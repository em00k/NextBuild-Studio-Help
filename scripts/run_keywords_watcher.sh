#!/bin/bash

# NextBuild Keywords Watcher Launcher
# Monitors keywords.json for changes and syncs to NextBuild Studio

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "NextBuild Keywords Watcher"
echo "=========================="
echo "Project root: $PROJECT_ROOT"
echo ""

# Default paths
SOURCE_FILE="$PROJECT_ROOT/data/keywords.json"
TARGET_FILE="/home/usb/Applications/NextBuildStudio/app/resources/app/extensions/em00k.nextbuild-viewers/data/keywords.json"

echo "Source: $SOURCE_FILE"
echo "Target: $TARGET_FILE"
echo ""

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed or not in PATH"
    exit 1
fi

# Check if source file exists
if [ ! -f "$SOURCE_FILE" ]; then
    echo "Error: Source file not found: $SOURCE_FILE"
    exit 1
fi

echo "Starting watcher..."
echo "Press Ctrl+C to stop"
echo ""

cd "$SCRIPT_DIR"
python3 keywords_watcher.py --source "$SOURCE_FILE" --target "$TARGET_FILE"

echo ""
echo "Keywords Watcher stopped."







