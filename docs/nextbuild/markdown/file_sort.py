#!/usr/bin/env python3
import os
import shutil
import sys


def organize_folder(source_dir, target_folders):
    # Ensure source exists
    if not os.path.isdir(source_dir):
        print(f"Error: '{source_dir}' is not a valid directory.")
        return

    # Create target folders if they don't exist
    for folder in target_folders:
        full_path = os.path.join(source_dir, folder)
        os.makedirs(full_path, exist_ok=True)

    # Prepare list of items excluding the target folders themselves
    existing = set(target_folders)
    items = [name for name in os.listdir(source_dir)
             if name not in existing]

    for name in items:
        src_path = os.path.join(source_dir, name)
        print(f"\nCurrent item: {name}")

        # Display options
        for idx, folder in enumerate(target_folders, start=1):
            print(f"  {idx}) {folder}")
        print("  0) Skip")

        # Prompt user
        choice = input("Choose destination number: ").strip()
        if not choice.isdigit():
            print("Invalid input, skipping.")
            continue

        idx = int(choice)
        if idx == 0:
            continue
        if 1 <= idx <= len(target_folders):
            dest_folder = os.path.join(source_dir, target_folders[idx-1])
            try:
                shutil.move(src_path, dest_folder)
                print(f"Moved '{name}' -> '{target_folders[idx-1]}'")
            except Exception as e:
                print(f"Error moving '{name}': {e}")
        else:
            print("Choice out of range, skipping.")


def main():
    # Read source directory (from argument or input)
    if len(sys.argv) > 1:
        source_dir = sys.argv[1]
    else:
        source_dir = input("Enter the path of the folder to organize: ").strip()

    # Define your target folders here (relative names)
    target_folders = [
        '1_constants',
        '2_keywords',
        '3_ports',
        '4_register',
        '5_nextlib'
    ]

    organize_folder(source_dir, target_folders)


if __name__ == '__main__':
    main()