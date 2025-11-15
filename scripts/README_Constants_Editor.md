# NextBuild Constants Editor

A Python GUI application for editing NextBuild constants JSON files.

## Features

- **Load and Save**: Open existing JSON constants files or create new ones
- **Edit Constants**: Modify constant names, values, and descriptions
- **Value Types**: Support for numbers, strings, booleans, and arrays
- **Navigate**: Use Previous/Next buttons or click on constants in the list
- **Search/Filter**: Search constants by name to quickly find what you're looking for
- **Create/Delete**: Add new constants or remove unwanted ones
- **Duplicate**: Copy existing constants as templates for new ones
- **Sort**: Sort constants by name or by value type
- **Auto-save**: Changes are tracked and can be saved back to JSON format

## Usage

### Running the Application

```bash
cd /path/to/nextbuild-viewers-linux/scripts
python3 nextbuild_constants_editor.py
```

Or make it executable and run directly:

```bash
./nextbuild_constants_editor.py
```

### Interface Overview

1. **Menu Bar**: File operations, editing commands, view options, and help
2. **Toolbar**: Quick access to common functions and sorting options
3. **Left Panel**: Constants list with search functionality and type information
4. **Right Panel**: Editor with fields for editing the selected constant
5. **Status Bar**: Current status and file information

### Editing Constants

1. **Constant Name**: The key identifier for the constant (must be unique)
2. **Value Type**: Choose from number, string, boolean, or array
3. **Value**: The actual value of the constant
   - **Number**: Integer or floating-point values
   - **String**: Text values (quotes are handled automatically)
   - **Boolean**: True/false values
   - **Array**: Multi-line list of values (one per line)
4. **Description**: Help text explaining what the constant represents

### Value Type Handling

- **Numbers**: Automatically detects integers vs. floating-point
- **Strings**: Handles quoted and unquoted strings
- **Booleans**: Accepts various formats (true/false, 1/0, yes/no)
- **Arrays**: Each line becomes an array element, with automatic type detection

### Keyboard Shortcuts

- `Ctrl+O`: Open file
- `Ctrl+S`: Save file
- `Ctrl+N`: New constant

## File Format

The application works with JSON files in the following format:

```json
{
  "CONSTANT_NAME": {
    "value": 42,
    "description": "An example numeric constant"
  },
  "STRING_CONSTANT": {
    "value": "Hello World",
    "description": "An example string constant"
  },
  "ARRAY_CONSTANT": {
    "value": [1, 2, 3, 4, 5],
    "description": "An example array constant"
  }
}
```

## Auto-Loading

The application automatically attempts to load `../data/nextbuild_constants.json` on startup if it exists.

## Sorting Options

- **Sort by Name**: Alphabetical sorting of constant names
- **Sort by Value**: Sorts by value type priority:
  1. Numbers (sorted numerically)
  2. Strings (sorted alphabetically)
  3. Booleans
  4. Arrays (sorted by length)
  5. Other types

## Notes

- Changes are made in memory until you save the file
- The constant name must be unique within the file
- Array values are parsed line-by-line with automatic type detection
- The application preserves JSON formatting and Unicode characters
- Empty descriptions are allowed but not recommended





