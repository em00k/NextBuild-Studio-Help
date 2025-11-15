#!/bin/bash

# NextBuild Keywords Editor Launcher
# This script launches the Python keywords editor GUI

SCRIPT_DIR="scripts"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "NextBuild Keywords Editor"
echo "========================"
echo "Project root: $PROJECT_ROOT"
echo ""

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed or not in PATH"
    exit 1
fi

# Check if tkinter is available
python3 -c "import tkinter" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Error: tkinter is not available. Please install it:"
    echo "  Ubuntu/Debian: sudo apt-get install python3-tk"
    echo "  CentOS/RHEL: sudo yum install tkinter"
    echo "  macOS: tkinter should be included with Python 3"
    echo "  Windows: tkinter should be included with Python 3"
    exit 1
fi

# Check if the keywords editor script exists
if [ ! -f "$SCRIPT_DIR/keywords_editor.py" ]; then
    echo "Error: keywords_editor.py not found in $SCRIPT_DIR"
    exit 1
fi

echo "Launching Keywords Editor..."
cd "$SCRIPT_DIR"
python3 keywords_editor.py jsonfiles/keywords.json

echo "Keywords Editor closed."







