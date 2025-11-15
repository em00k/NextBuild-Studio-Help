/*
 * Script: md-to-snippets.js
 *
 * Two-way converter for VS Code snippets:
 * 1) Markdown folder -> JSON snippets file
 * 2) JSON snippets file -> Markdown files
 *
 * Now handles cases where `body` may be a string or array.
 *
 * Expectations for Markdown files:
 * - YAML frontmatter with keys:
 *     name:        snippet key (e.g. "WaitRaster(nn)")
 *     prefix:      snippet prefix (e.g. "WaitRaster")
 *     description: snippet description
 * - Single fenced code block containing the snippet body
 *
 * Usage:
 *   npm install gray-matter fs-extra
 *   node md-to-snippets.js <input> <output>
 *
 * Behavior:
 * - If <input> is a directory: read all .md, convert to JSON and write to <output> (file).
 * - If <input> is a .json file: read JSON, create a folder at <output> and write one .md per snippet.
 */

const fs = require('fs');
const path = require('path');
const matter = require('gray-matter');
const fse = require('fs-extra');

if (process.argv.length < 4) {
  console.error('Usage: node md-to-snippets.js <input> <output>');
  process.exit(1);
}

const input = path.resolve(process.argv[2]);
const output = path.resolve(process.argv[3]);

function mdFolderToJson(mdDir, outFile) {
  const snippets = {};
  fs.readdirSync(mdDir).forEach(file => {
    if (path.extname(file).toLowerCase() !== '.md') return;
    const fullPath = path.join(mdDir, file);
    const text = fs.readFileSync(fullPath, 'utf8');
    const { data, content: mdBody } = matter(text);
    const codeMatch = /```[\w+]*\n([\s\S]*?)```/.exec(mdBody);
    if (!codeMatch) {
      console.warn(`Skipping ${file}: no code block`);
      return;
    }
    const bodyLines = codeMatch[1].split(/\r?\n/);
    const key = data.name || path.basename(file, '.md');
    snippets[key] = {
      prefix: data.prefix || key,
      body: bodyLines,
      description: data.description || ''
    };
  });
  fs.writeFileSync(outFile, JSON.stringify(snippets, null, 2));
  console.log(`Wrote ${Object.keys(snippets).length} snippets to ${outFile}`);
}

function jsonToMdFiles(jsonFile, outDir) {
  const content = fs.readFileSync(jsonFile, 'utf8');
  const snippets = JSON.parse(content);
  fse.ensureDirSync(outDir);
  Object.entries(snippets).forEach(([name, def]) => {
    const mdName = `${name.replace(/[^a-z0-9_-]/gi, '_')}.md`;
    const filePath = path.join(outDir, mdName);
    const frontmatter = {
      name,
      prefix: def.prefix || name,
      description: def.description || ''
    };

    // Normalize body to array of lines
    let bodyLines;
    if (Array.isArray(def.body)) {
      bodyLines = def.body;
    } else if (typeof def.body === 'string') {
      bodyLines = def.body.split(/\r?\n/);
    } else {
      console.warn(`Snippet ${name} has no valid body; skipping.`);
      return;
    }

    // Trim any empty trailing lines
    if (bodyLines.length && bodyLines[bodyLines.length - 1] === '') {
      bodyLines.pop();
    }

    const bodyBlock = bodyLines.join('\n');
    const mdContent = matter.stringify(`
\`\`\`
${bodyBlock}
\`\`\`
`, frontmatter);
    fs.writeFileSync(filePath, mdContent.trimStart());
    console.log(`Created ${filePath}`);
  });
}

// Determine mode
const stat = fs.statSync(input);
if (stat.isDirectory()) {
  mdFolderToJson(input, output);
} else if (path.extname(input).toLowerCase() === '.json') {
  jsonToMdFiles(input, output);
} else {
  console.error('Input must be a folder of Markdown files or a .json snippet file');
  process.exit(1);
}
