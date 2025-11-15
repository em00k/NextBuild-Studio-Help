/*
 * Script: md-to-snippets.js
 *
 * Reads all Markdown files in a folder, expects each file to include YAML frontmatter with:
 *   name:        snippet key (e.g. "WaitRaster(nn)")
 *   prefix:      the snippet prefix (e.g. "WaitRaster")
 *   description: snippet description
 *
 * And a fenced code block containing the body lines.
 *
 * Outputs a single JSON file with VS Code snippets:
 * {
 *   "SnippetName": { "prefix": ..., "body": [...], "description": ... },
 *   ...
 * }
 *
 * Usage:
 *   npm install gray-matter
 *   node md-to-snippets.js <input-folder> <output-file>
 */

const fs = require('fs');
const path = require('path');
const matter = require('gray-matter');

if (process.argv.length < 4) {
  console.error('Usage: node md-to-snippets.js <input-folder> <output-file>');
  process.exit(1);
}

const inputDir = path.resolve(process.argv[2]);
const outputFile = path.resolve(process.argv[3]);

let snippets = {};

fs.readdirSync(inputDir).forEach(file => {
  if (path.extname(file).toLowerCase() !== '.md') {return;}

  const fullPath = path.join(inputDir, file);
  const content = fs.readFileSync(fullPath, 'utf8');
  const { data, content: mdBody } = matter(content);

  // Expect a single fenced code block for the snippet body
  const codeFenceMatch = /```[\w+]*\n([\s\S]*?)```/.exec(mdBody);
  if (!codeFenceMatch) {
    console.warn(`Skipping ${file}: no code fence found`);
    return;
  }

  const bodyLines = codeFenceMatch[1]
    .split("\n")
    .map(line => line.replace(/\r?$/, ''));

  const key = data.name || path.basename(file, '.md');
  snippets[key] = {
    prefix: data.prefix || key,
    body: bodyLines,
    description: data.description || ''
  };
});

// Write JSON with 2-space indentation
fs.writeFileSync(outputFile, JSON.stringify(snippets, null, 2));
console.log(`Wrote ${Object.keys(snippets).length} snippets to ${outputFile}`);
