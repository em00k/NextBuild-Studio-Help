#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

/**
 * Converts a markdown template file to JSON format compatible with the extension
 * Usage: node template-converter.js input.md [output.json]
 */

function parseMarkdownTemplate(content) {
    const lines = content.split('\n');
    let currentSection = null;
    let currentFile = null;
    let currentCodeBlock = false;
    let currentCodeLanguage = '';
    
    const template = {
        name: '',
        description: '',
        type: 'custom',
        directories: [],
        files: []
    };
    
    for (let i = 0; i < lines.length; i++) {
        const line = lines[i];
        const trimmed = line.trim();
        
        // Parse template name and description
        if (trimmed.startsWith('# Template Name:')) {
            template.name = trimmed.substring(16).trim();
        } else if (trimmed.startsWith('Description:')) {
            template.description = trimmed.substring(12).trim();
        }
        
        // Parse sections
        else if (trimmed === '## Directories') {
            currentSection = 'directories';
        } else if (trimmed === '## Files') {
            currentSection = 'files';
        }
        
        // Parse directories
        else if (currentSection === 'directories' && trimmed.startsWith('-')) {
            const dir = trimmed.substring(1).trim();
            template.directories.push(dir);
        }
        
        // Parse file definitions
        else if (currentSection === 'files' && trimmed.startsWith('###')) {
            if (currentFile) {
                // Save previous file
                template.files.push(currentFile);
            }
            
            // Start new file
            const fileName = trimmed.substring(3).trim();
            currentFile = {
                name: fileName,
                template: ''
            };
        }
        
        // Parse code blocks
        else if (trimmed.startsWith('```')) {
            if (!currentCodeBlock) {
                currentCodeBlock = true;
                currentCodeLanguage = trimmed.substring(3);
            } else {
                currentCodeBlock = false;
                currentCodeLanguage = '';
            }
        }
        
        // Collect file content
        else if (currentFile && currentCodeBlock) {
            if (currentFile.template) {
                currentFile.template += '\n';
            }
            currentFile.template += line;
        }
    }
    
    // Add the last file if it exists
    if (currentFile) {
        template.files.push(currentFile);
    }
    
    // Template content is ready - JSON.stringify will handle escaping
    
    return template;
}

function convertTemplate(inputFile, outputFile) {
    try {
        console.log(`Converting ${inputFile} to JSON template...`);
        
        // Read markdown file
        const content = fs.readFileSync(inputFile, 'utf8');
        
        // Parse the markdown
        const template = parseMarkdownTemplate(content);
        
        // Validate template
        if (!template.name) {
            throw new Error('Template name is required');
        }
        
        if (!template.description) {
            throw new Error('Template description is required');
        }
        
        if (template.files.length === 0) {
            throw new Error('At least one file must be defined');
        }
        
        // Generate output filename if not provided
        if (!outputFile) {
            const baseName = path.basename(inputFile, '.md');
            outputFile = path.join(path.dirname(inputFile), `${baseName}.json`);
        }
        
        // Write JSON file
        fs.writeFileSync(outputFile, JSON.stringify(template, null, 4), 'utf8');
        
        console.log(`✅ Successfully converted to ${outputFile}`);
        console.log(`📋 Template: ${template.name}`);
        console.log(`📝 Description: ${template.description}`);
        console.log(`📁 Directories: ${template.directories.length}`);
        console.log(`📄 Files: ${template.files.length}`);
        
    } catch (error) {
        console.error(`❌ Error converting template: ${error.message}`);
        process.exit(1);
    }
}

function showHelp() {
    console.log(`
NextBuild Template Converter
============================

Converts markdown template files to JSON format for NextBuild extension.

Usage:
  node template-converter.js <input.md> [output.json]

Examples:
  node template-converter.js my-template.md
  node template-converter.js my-template.md custom-output.json

Markdown Format:
  # Template Name: Your Template Name
  Description: Your template description

  ## Directories
  - directory1
  - directory2/subdirectory

  ## Files

  ### filename.ext
  \`\`\`language
  file content here
  use {projectName} as placeholder
  \`\`\`

  ### another-file.txt
  \`\`\`
  more content
  \`\`\`
`);
}

// Main execution
const args = process.argv.slice(2);

if (args.length === 0 || args[0] === '--help' || args[0] === '-h') {
    showHelp();
    process.exit(0);
}

const inputFile = args[0];
const outputFile = args[1];

if (!fs.existsSync(inputFile)) {
    console.error(`❌ Input file not found: ${inputFile}`);
    process.exit(1);
}

convertTemplate(inputFile, outputFile); 