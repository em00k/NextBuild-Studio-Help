#!/bin/bash
# NextBuild Constants Editor Launcher

cd "$(dirname "$0")"

if command -v python3 &> /dev/null; then
    python3 nextbuild_constants_editor.py
elif command -v python &> /dev/null; then
    python nextbuild_constants_editor.py
else
    echo "Python is not installed or not in PATH"
    echo "Please install Python 3 and try again"
    exit 1
fi





