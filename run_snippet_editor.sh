#!/bin/bash
# NextBuild Snippets Editor Launcher

cd scripts

if command -v python3 &> /dev/null; then
    python3 nextbuild_snippet_editor.py
elif command -v python &> /dev/null; then
    python nextbuild_snippet_editor.py
else
    echo "Python is not installed or not in PATH"
    echo "Please install Python 3 and try again"
    exit 1
fi





