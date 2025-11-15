#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

/**
 * Converts a JSON template file to markdown format
 * Usage: node json-to-template-md.js input.json [output.md]
 */

function convertJsonToMarkdown(template) {
    let markdown = '';
    
    // Header with template name and description
    markdown += `# Template Name: ${template.name}\n`;
    markdown += `Description: ${template.description}\n\n`;
    
    // Directories section
    if (template.directories && template.directories.length > 0) {
        markdown += `## Directories\n`;
        template.directories.forEach(dir => {
            markdown += `- ${dir}\n`;
        });
        markdown += '\n';
    }
    
    // Files section
    if (template.files && template.files.length > 0) {
        markdown += `## Files\n\n`;
        
        template.files.forEach(file => {
            markdown += `### ${file.name}\n`;
            
            // Determine language from file extension
            const ext = path.extname(file.name).toLowerCase();
            let language = '';
            switch (ext) {
                case '.bas':
                    language = 'nextbuild';
                    break;
                case '.js':
                    language = 'javascript';
                    break;
                case '.json':
                    language = 'json';
                    break;
                case '.txt':
                    language = '';
                    break;
                default:
                    language = '';
            }
            
            markdown += '```' + language + '\n';
            
            // Convert escaped content back to normal
            const content = file.template
                .replace(/\\n/g, '\n')
                .replace(/\\"/g, '"');
            
            markdown += content;
            markdown += '\n```\n\n';
        });
    }
    
    return markdown;
}

function convertTemplate(inputFile, outputFile) {
    try {
        console.log(`Converting ${inputFile} to markdown template...`);
        
        // Read JSON file
        const content = fs.readFileSync(inputFile, 'utf8');
        const template = JSON.parse(content);
        
        // Convert to markdown
        const markdown = convertJsonToMarkdown(template);
        
        // Generate output filename if not provided
        if (!outputFile) {
            const baseName = path.basename(inputFile, '.json');
            outputFile = path.join(path.dirname(inputFile), `${baseName}.md`);
        }
        
        // Write markdown file
        fs.writeFileSync(outputFile, markdown, 'utf8');
        
        console.log(`✅ Successfully converted to ${outputFile}`);
        console.log(`📋 Template: ${template.name}`);
        console.log(`📝 Description: ${template.description}`);
        if (template.directories) {
            console.log(`📁 Directories: ${template.directories.length}`);
        }
        if (template.files) {
            console.log(`📄 Files: ${template.files.length}`);
        }
        
    } catch (error) {
        console.error(`❌ Error converting template: ${error.message}`);
        process.exit(1);
    }
}

function showHelp() {
    console.log(`
NextBuild JSON to Markdown Template Converter
==============================================

Converts JSON template files back to markdown format.

Usage:
  node json-to-template-md.js <input.json> [output.md]

Examples:
  node json-to-template-md.js multi-file.json
  node json-to-template-md.js multi-file.json custom-output.md
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