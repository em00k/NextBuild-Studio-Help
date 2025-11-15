#!/bin/bash
# NextBuild Editor Menu
# A menu-driven launcher for NextBuild editors

source venv/bin/activate

# Function to display the menu
show_menu() {
    echo "========================================"
    echo "     NextBuild Editor Launcher"
    echo "========================================"
    echo ""
    echo "Available Editors:"
    echo "  1) Keywords Editor     (jsonfiles/keywords.json)"
    echo "  2) Constants Editor    (jsonfiles/nextbuild.json)"
    echo "  3) Snippets Editor     (jsonfiles/nextbuild.json)"
    echo "  4) Copy to Live        (copy_to_live.sh)"
    echo ""
    echo "  0) Exit"
    echo ""
    echo -n "Select an editor (1-4) or 0 to exit: "
}

# Function to run keywords editor
run_keywords_editor() {
    echo ""
    echo "Launching Keywords Editor..."
    echo "=========================="


    # Launch the editor
    cd scripts
    python3 keywords_editor.py ../jsonfiles/keywords.json
    cd ..
    echo "Keywords Editor closed."
}

# Function to run constants editor
run_constants_editor() {
    echo ""
    echo "Launching Constants Editor..."
    echo "==========================="

    # Launch the editor
    cd scripts
    python3 nextbuild_constants_editor.py ../jsonfiles/nextbuild_constants.json
    cd ..
    echo "Constants Editor closed."
}

# Function to run snippets editor
run_snippets_editor() {
    echo ""
    echo "Launching Snippets Editor..."
    echo "=========================="

    # Launch the editor
    cd scripts
    python3 nextbuild_snippet_editor.py ../jsonfiles/nextbuild_snippets.json
    cd ..
    echo "Snippets Editor closed."
}

# Function to copy to live
copy_to_live() {
    echo ""
    echo "Copying to live..."
    echo "=================="
    ./copy_to_live.sh
    echo "Copy to live closed."
}

# Main menu loop
while true; do
    show_menu
    read choice

    case $choice in
        1|keywords|Keywords|KEYWORDS)
            run_keywords_editor
            ;;
        2|constants|Constants|CONSTANTS)
            run_constants_editor
            ;;
        3|snippets|Snippets|SNIPPETS)
            run_snippets_editor
            ;;
        4|copy_to_live|CopyToLive|COPY_TO_LIVE)
            copy_to_live
            ;;
        0|exit|Exit|EXIT|quit|Quit|QUIT)
            echo ""
            echo "Goodbye!"
            exit 0
            ;;
        *)
            echo ""
            echo "Invalid choice. Please select 1-4 or 0 to exit."
            echo "You can also type 'keywords', 'constants', or 'snippets'."
            echo ""
            read -p "Press Enter to continue..."
            ;;
    esac

    # Add a blank line between runs
    echo ""
done
