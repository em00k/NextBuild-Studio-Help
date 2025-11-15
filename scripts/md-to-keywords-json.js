/**
 * MD to Keywords JSON Converter
 * 
 * This script converts markdown documentation files into a JSON structure
 * that can be used by the VS Code extension for keyword help.
 * 
 * How it works:
 * 1. Recursively scans all .md files in docs/nextbuild/markdown/
 * 2. For each markdown file:
 *    - Creates a key from filename (uppercase, without .md extension)
 *    - Determines category from the folder name
 *    - Checks for YAML frontmatter and looks for 'isManualOnly: true' flag
 *    - Strips frontmatter from content if present
 *    - Determines if file should be manual-only based on:
 *      * Files starting with underscore (_)
 *      * Files in "manuals/" directory
 *      * Files in "reference/" directory
 *      * Files with frontmatter flag 'isManualOnly: true'
 * 3. Creates JSON entry with: content, category, showInKeywordList, isManualOnly
 * 4. Outputs to data/keywords.json
 * 
 * Manual-only behavior (isManualOnly: true):
 * - ❌ NOT shown in autocomplete/IntelliSense
 * - ❌ NOT shown in hover help
 * - ❌ NOT shown in "All Available Keywords" section
 * - ✅ Still accessible via F1 search (part of help system)
 * 
 * Regular keywords (isManualOnly: false):
 * - ✅ Shown in autocomplete/IntelliSense
 * - ✅ Shown in hover help
 * - ✅ Shown in "All Available Keywords" section
 * - ✅ Accessible via F1 search
 */

const fs = require('fs');
const path = require('path');

const inputDir = path.join(__dirname, '../docs/nextbuild/markdown');
const outputFile = path.join(__dirname, '../data/keywords.json');

const result = {};

// Recursively process files in directories
function processDirectory(dir) {
  fs.readdirSync(dir, { withFileTypes: true }).forEach(entry => {
    const fullPath = path.join(dir, entry.name);
    
    if (entry.isDirectory()) {
      processDirectory(fullPath); // Process subdirectories
      return;
    }
    
    if (!entry.name.endsWith('.md')) {
      return; // Skip non-markdown files
    }
    
    // Read the file
    const content = fs.readFileSync(fullPath, 'utf8');
    
    // Generate the key
    const key = path.basename(entry.name, '.md').toUpperCase();
    
    // Determine the category from the folder name
    const relativePath = path.relative(inputDir, dir);
    const category = relativePath.split(path.sep)[0] || 'manual';
    
    // Check for frontmatter flag and strip it from content
    let hasManualOnlyFlag = false;
    let cleanContent = content;
    
    if (content.startsWith('---\n')) {
      // Extract frontmatter section - look for closing --- with optional spaces/newlines
      const frontmatterMatch = content.match(/^---\n([\s\S]*?)\n---\s*\n/);
      if (frontmatterMatch) {
        const frontmatter = frontmatterMatch[1];
        // Check for isManualOnly flag in frontmatter
        hasManualOnlyFlag = /^isManualOnly:\s*true\s*$/m.test(frontmatter);
        // Remove frontmatter from content
        cleanContent = content.replace(frontmatterMatch[0], '').trim();
      }
    }
    
    // Determine if this file should be manual-only
    // Normalize path separators and check for directory names
    const normalizedPath = relativePath.replace(/\\/g, '/').toLowerCase();
    const isManualOnly = 
      entry.name.startsWith('_') ||            // Files starting with underscore
      normalizedPath.includes('manuals') ||    // Files in a "manuals" directory
      normalizedPath.includes('reference') ||  // Files in a "reference" directory 
      hasManualOnlyFlag;                       // Files with frontmatter flag
    
    // Create entry
    result[key] = {
      content: cleanContent,
      category: category,
      showInKeywordList: false,
      isManualOnly: isManualOnly
    };
    console.log(`Processed: ${entry.name} (isManualOnly: ${isManualOnly})`);
  });
}

// Start processing files
processDirectory(inputDir);

fs.writeFileSync(outputFile, JSON.stringify(result, null, 2));
console.log(`keywords.json generated with ${Object.keys(result).length} entries!`); 