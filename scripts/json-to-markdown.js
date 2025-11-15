// This script converts a JSON file to a markdown file
// It is used to convert the AYFX.json file to a markdown file
// It is used to convert the AYFX_help.json file to a markdown file

const fs = require('fs');
const path = require('path');

function jsonToMarkdown(inputFile, outputFile = null) {
    try {
        // Read the JSON file
        const jsonData = JSON.parse(fs.readFileSync(inputFile, 'utf8'));
        
        // If no output file specified, create one based on input filename
        if (!outputFile) {
            const inputPath = path.parse(inputFile);
            outputFile = path.join(inputPath.dir, inputPath.name + '.md');
        }
        
        // Extract markdown content from the first key's content field
        const firstKey = Object.keys(jsonData)[0];
        const markdownContent = jsonData[firstKey].content;
        
        if (!markdownContent) {
            throw new Error('No content field found in JSON structure');
        }
        
        // Write the markdown file
        fs.writeFileSync(outputFile, markdownContent, 'utf8');
        
        console.log(`✅ Successfully converted ${inputFile} to ${outputFile}`);
        console.log(`📄 Extracted content from key: ${firstKey}`);
        
    } catch (error) {
        console.error('❌ Error converting JSON to markdown:', error.message);
        process.exit(1);
    }
}

// Get command line arguments
const args = process.argv.slice(2);

if (args.length === 0) {
    console.log('Usage: node json-to-markdown.js <input.json> [output.md]');
    console.log('Example: node json-to-markdown.js AYFX.json AYFX.md');
    process.exit(1);
}

const inputFile = args[0];
const outputFile = args[1];

// Check if input file exists
if (!fs.existsSync(inputFile)) {
    console.error(`❌ Input file not found: ${inputFile}`);
    process.exit(1);
}

jsonToMarkdown(inputFile, outputFile); 