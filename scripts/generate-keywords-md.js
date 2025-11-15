const fs = require('fs');
const path = require('path');

const keywordsFile = path.join(__dirname, '../data/keywords.json');

// Read the keywords.json file
const keywords = JSON.parse(fs.readFileSync(keywordsFile, 'utf8'));

// Group keywords by category
const categories = {};
Object.entries(keywords).forEach(([key, data]) => {
  const category = data.category;
  if (!categories[category]) {
    categories[category] = [];
  }
  categories[category].push(key);
});

// Sort categories and keywords within each category
const sortedCategories = Object.keys(categories).sort();
sortedCategories.forEach(category => {
  categories[category].sort();
});

// Generate markdown files for each category
sortedCategories.forEach(category => {
  const categoryFile = path.join(__dirname, '..', `${category}.md`);
  let markdownContent = `# ${category.charAt(0).toUpperCase() + category.slice(1)}\n\n`;
  
  categories[category].forEach(keyword => {
    const filename = keyword.toLowerCase() + '.md';
    markdownContent += `\`\`\`${keyword}\`\`\` [${keyword}](${filename})\n\n`;
  });
  
  fs.writeFileSync(categoryFile, markdownContent);
  console.log(`${category}.md generated with ${categories[category].length} entries!`);
});

console.log(`\nGenerated ${sortedCategories.length} category files with ${Object.keys(keywords).length} total entries!`);
console.log(`Categories: ${sortedCategories.join(', ')}`);

// Show the file list
sortedCategories.forEach(category => {
  console.log(`  ${category}.md - ${categories[category].length} entries`);
}); 