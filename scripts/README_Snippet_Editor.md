# NextBuild Snippets Editor

A Python GUI application for editing NextBuild JSON snippet files.

## Features

- **Load and Save**: Open existing JSON snippet files or create new ones
- **Edit Snippets**: Modify snippet names, prefixes, body content, and descriptions
- **Navigate**: Use Previous/Next buttons or click on snippets in the list
- **Search/Filter**: Search snippets by name to quickly find what you're looking for
- **Create/Delete**: Add new snippets or remove unwanted ones
- **Duplicate**: Copy existing snippets as templates for new ones
- **Auto-save**: Changes are tracked and can be saved back to JSON format

## Usage

### Running the Application

```bash
cd /path/to/nextbuild-viewers-linux/scripts
python3 nextbuild_snippet_editor.py
```

Or make it executable and run directly:

```bash
./nextbuild_snippet_editor.py
```

### Interface Overview

1. **Menu Bar**: File operations, editing commands, and help
2. **Toolbar**: Quick access to common functions
3. **Left Panel**: Snippet list with search functionality
4. **Right Panel**: Editor for the selected snippet
5. **Status Bar**: Current status and file information

### Editing Snippets

1. **Snippet Name**: The key identifier for the snippet
2. **Prefix**: The trigger text that activates the snippet
3. **Body**: The code template (one line per array element)
4. **Description**: Help text explaining what the snippet does

### Keyboard Shortcuts

- `Ctrl+O`: Open file
- `Ctrl+S`: Save file
- `Ctrl+N`: New snippet

## File Format

The application works with JSON files in the following format:

```json
{
  "Snippet Name": {
    "prefix": "trigger_text",
    "body": [
      "line 1 of code",
      "line 2 of code",
      "$0"
    ],
    "description": "Description of what this snippet does"
  }
}
```

## Dependencies

- Python 3.x
- tkinter (usually included with Python)
- json (standard library)
- os, pathlib (standard library)

## Auto-Loading

The application automatically attempts to load `../snippets/nextbuild.json` on startup if it exists.

## Notes

- Changes are made in memory until you save the file
- The body field supports multi-line editing with each line becoming an array element
- Use the search box to quickly filter through many snippets
- Renaming a snippet will update its key in the JSON structure
