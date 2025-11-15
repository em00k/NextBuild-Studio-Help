# NextBuild Keywords Editor

A comprehensive GUI application for editing NextBuild keywords JSON files with full CRUD (Create, Read, Update, Delete) functionality.

## Features

### Core Functionality
- **Load and Save**: Open existing keywords.json files or create new ones
- **Add Keywords**: Create new keywords with default templates
- **Edit Keywords**: Modify all properties of existing keywords
- **Delete Keywords**: Remove unwanted keywords
- **Duplicate Keywords**: Clone existing keywords for quick creation
- **Content Cleaning**: Remove trailing whitespace and non-printable characters
- **Markdown Formatting**: Auto-format markdown syntax and structure

### Advanced Features
- **Search**: Real-time search through keyword names
- **Filter by Category**: Filter keywords by category (keywords, manual, esxdos, nextlib, constants)
- **Live Editing**: Changes are reflected immediately in the data structure
- **Auto-save**: Save your work with keyboard shortcuts
- **Sort Options**: Sort keywords alphabetically or by category
- **Tabbed Content Editor**: Switch between "Edit" and "Preview" modes
- **Markdown Preview**: See formatted markdown output in real-time

### Keyword Properties
Each keyword can have the following properties:

- **Keyword Name**: The identifier/key for the keyword
- **Content**: Markdown-formatted documentation content
- **Category**: Classification (keywords, manual, esxdos, nextlib, constants)
- **Show in Keyword List**: Boolean flag for keyword list visibility
- **Manual Only**: Boolean flag for manual-only keywords

## Installation & Requirements

### Prerequisites
- Python 3.6+
- tkinter (usually included with Python 3)
- Linux/Windows/macOS

### Installing tkinter (if needed)
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# CentOS/RHEL
sudo yum install tkinter

# macOS - usually included with Python 3
# Windows - usually included with Python 3
```

## Usage

### Running the Editor

#### Method 1: Using the launcher script (Recommended)
```bash
cd /path/to/nextbuild-viewers-linux/scripts
./run_keywords_editor.sh
```

#### Method 2: Direct Python execution
```bash
cd /path/to/nextbuild-viewers-linux/scripts
python3 keywords_editor.py
```

### Interface Overview

#### Main Window Layout
- **Menu Bar**: File, Edit, View, Help menus
- **Toolbar**: Quick access buttons for common operations
- **Search/Filter Bar**: Search keywords and filter by category
- **Keywords List (Left)**: Scrollable list of all keywords
- **Editor Panel (Right)**: Edit the selected keyword's properties
  - **Content Tools**: Clean Content and Format Markdown buttons
  - **Content Tabs**: Edit tab (raw markdown) and Preview tab (formatted view)
- **Status Bar**: Shows current status and information

#### Keyboard Shortcuts
- `Ctrl+O`: Open file
- `Ctrl+S`: Save file
- `Ctrl+N`: New keyword
- `Ctrl+D`: Duplicate keyword
- `Delete`: Delete selected keyword

### Basic Workflow

1. **Launch the Editor**
   ```bash
   ./run_keywords_editor.sh
   ```

2. **Auto-load Default File**
   - The editor automatically loads `../data/keywords.json` if it exists

3. **Create a New Keyword**
   - Click "New" button or press `Ctrl+N`
   - Edit the keyword name, category, and content
   - The editor provides a basic markdown template

4. **Edit an Existing Keyword**
   - Select a keyword from the list
   - Modify any property in the editor panel
   - Changes are saved to memory immediately

5. **Search and Filter**
   - Use the search box to find keywords by name
   - Use the category dropdown to filter by type

6. **Save Your Work**
   - Click "Save" or press `Ctrl+S`
   - The editor supports both save and save-as operations

### Content Editing Features

#### Content Cleaning
The **Clean Content** button removes common formatting issues:
- Trailing whitespace from each line
- Non-printable characters that appear as "empty boxes"
- Multiple consecutive empty lines (reduces to maximum 2)
- Preserves intentional formatting and line breaks

#### Markdown Formatting
The **Format Markdown** button automatically improves markdown structure:
- Ensures proper spacing around headers (`#` becomes `# `)
- Adds blank lines before headers when needed
- Formats list markers consistently (`-` vs `*` vs numbered lists)
- Standardizes code block formatting

#### Preview Mode
Switch to the **Preview** tab to see formatted markdown output:
- Headers are displayed with underlines
- Lists show bullet points
- Code blocks are clearly marked
- Links show as "text (link)" format
- Auto-updates when you edit content in the Edit tab

#### Right-Click Context Menu
Right-click anywhere in the content editor to access the keyword linking dialog:
- **Searchable list**: Type to filter keywords in real-time
- **Scrollable interface**: Handles 400+ keywords without screen overflow
- **Smart filtering**: Current keyword is excluded to prevent self-reference
- **Live count**: Shows number of keywords/matches displayed
- **Keyboard shortcuts**: Enter key or double-click to insert
- **Proper formatting**: Keywords are automatically converted to lowercase for .md files

#### Keyboard Shortcuts
- **Ctrl+K**: Quick access to keyword linking dialog (when editing content)
- **Ctrl+S**: Save file
- **Ctrl+O**: Open file
- **Ctrl+N**: New keyword
- **Ctrl+D**: Duplicate keyword
- **Delete**: Delete selected keyword

### Cleaning Your Keywords File

Use the companion script to clean your entire keywords file:

```bash
cd scripts
python3 clean_keywords_content.py
```

This will:
- Analyze all 426+ keywords for issues
- Create a backup file automatically
- Remove thousands of problematic characters
- Show detailed statistics of what was cleaned

### Advanced Usage

#### Content Editing
The content field supports Markdown formatting. Common patterns:

```markdown
# Keyword Name

## Description
Description of the keyword...

## Syntax
```
usage syntax here
```

## Examples
```
example code here
```

## Remarks
Additional notes...
```

#### Categories
- **keywords**: Standard language keywords
- **manual**: Manual/documentation entries
- **esxdos**: ESXDOS API functions
- **nextlib**: NextLib functions
- **constants**: Constant definitions

#### Boolean Flags
- **Show in Keyword List**: Controls visibility in IDE keyword lists
- **Manual Only**: Marks entries that appear only in manuals

## File Structure

```
scripts/
├── keywords_editor.py          # Main editor application
├── run_keywords_editor.sh      # Launcher script
└── README_Keywords_Editor.md   # This documentation

data/
└── keywords.json              # Default keywords file
```

## Troubleshooting

### Common Issues

1. **"tkinter not found" error**
   ```bash
   # Install tkinter for your system
   sudo apt-get install python3-tk  # Ubuntu/Debian
   ```

2. **Permission denied when saving**
   - Ensure write permissions on the target directory
   - Try "Save As" to save to a different location

3. **Large files load slowly**
   - The editor is optimized for large JSON files
   - Search and filter operations help manage large datasets

4. **GUI doesn't appear**
   - Ensure you're running in a graphical environment
   - Check that DISPLAY variable is set (Linux)

### Performance Tips

- Use search and filter to work with subsets of large files
- Sort operations help organize keywords logically
- The editor maintains all data in memory for fast operations

## Technical Details

### Dependencies
- `json`: For JSON file handling
- `tkinter`: GUI framework
- `pathlib`: Path operations
- `os`: File system operations

### Data Format
The editor expects JSON files with this structure:
```json
{
  "KEYWORD_NAME": {
    "content": "# Markdown content...",
    "category": "keywords",
    "showInKeywordList": false,
    "isManualOnly": false
  }
}
```

### Architecture
- **Model**: Dictionary-based data storage
- **View**: tkinter-based GUI components
- **Controller**: Event handlers and business logic
- **Persistence**: JSON file I/O operations

## Contributing

To extend the keywords editor:

1. **Add new categories**: Update the category dropdown values
2. **Enhance editing**: Add validation or preview features
3. **Improve UI**: Modify layouts or add themes
4. **Add export options**: Support different output formats

## License

This tool is part of the NextBuild project. See project LICENSE for details.

## Support

For issues or questions:
1. Check this README for common solutions
2. Review the existing Python editors for patterns
3. Test with small JSON files first
4. Ensure Python 3 and tkinter are properly installed
