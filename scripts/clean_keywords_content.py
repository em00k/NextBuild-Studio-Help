#!/usr/bin/env python3
"""
NextBuild Keywords Content Cleaner
A utility script to clean and fix issues in keywords.json content
"""

import json
import re
import os
from pathlib import Path

def clean_content_text(content):
    """Clean content text by removing problematic characters"""
    if not content:
        return content

    original_content = content

    # Remove trailing whitespace from each line
    lines = content.split('\n')
    cleaned_lines = []
    for line in lines:
        # Remove trailing whitespace but preserve intentional spacing
        cleaned_line = line.rstrip()
        cleaned_lines.append(cleaned_line)

    # Rejoin lines, preserving final newline if it existed
    content = '\n'.join(cleaned_lines)
    if original_content.endswith('\n'):
        content += '\n'

    # Remove any non-printable characters (except newlines, tabs, and common whitespace)
    # This will catch characters that appear as "boxes" or other symbols
    content = re.sub(r'[^\x20-\x7E\n\t\r]', '', content)

    # Clean up excessive whitespace
    # Remove multiple consecutive empty lines (more than 2)
    content = re.sub(r'\n{3,}', '\n\n', content)

    # Remove trailing spaces before newlines
    content = re.sub(r' +\n', '\n', content)

    return content

def analyze_keywords_file(file_path):
    """Analyze the keywords file for issues"""
    print(f"Analyzing keywords file: {file_path}")
    print("=" * 50)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        total_keywords = len(data)
        issues_found = 0
        cleaned_count = 0

        print(f"Total keywords found: {total_keywords}")
        print()

        # Check each keyword for issues
        for keyword, info in data.items():
            content = info.get('content', '')
            original_content = content

            # Clean the content
            cleaned_content = clean_content_text(content)

            # Check for issues
            issues = []

            # Check for non-printable characters
            non_printable = re.findall(r'[^\x20-\x7E\n\t\r]', content)
            if non_printable:
                issues.append(f"Non-printable chars: {len(non_printable)}")

            # Check for trailing whitespace
            lines_with_trailing_space = 0
            for line in content.split('\n'):
                if line.rstrip() != line:
                    lines_with_trailing_space += 1
            if lines_with_trailing_space > 0:
                issues.append(f"Lines with trailing whitespace: {lines_with_trailing_space}")

            # Check for excessive empty lines
            empty_lines = re.findall(r'\n{3,}', content)
            if empty_lines:
                issues.append(f"Excessive empty lines: {len(empty_lines)}")

            if issues:
                issues_found += 1
                print(f"Keyword '{keyword}':")
                for issue in issues:
                    print(f"  - {issue}")

                if cleaned_content != original_content:
                    cleaned_count += 1
                    print(f"  ✓ Content cleaned (removed {len(original_content) - len(cleaned_content)} chars)")
                print()

        print("Summary:")
        print(f"- Total keywords: {total_keywords}")
        print(f"- Keywords with issues: {issues_found}")
        print(f"- Keywords cleaned: {cleaned_count}")

        return data

    except Exception as e:
        print(f"Error analyzing file: {e}")
        return None

def clean_keywords_file(file_path, backup=True):
    """Clean all content in the keywords file"""
    print(f"Cleaning keywords file: {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Create backup
        if backup:
            backup_path = file_path + '.backup'
            with open(backup_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"Backup created: {backup_path}")

        total_cleaned = 0
        total_chars_removed = 0

        # Clean each keyword's content
        for keyword, info in data.items():
            if 'content' in info:
                original_content = info['content']
                cleaned_content = clean_content_text(original_content)

                if cleaned_content != original_content:
                    chars_removed = len(original_content) - len(cleaned_content)
                    total_chars_removed += chars_removed
                    total_cleaned += 1

                    info['content'] = cleaned_content

        # Save cleaned file
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print("Cleaning completed:")
        print(f"- Keywords cleaned: {total_cleaned}")
        print(f"- Total characters removed: {total_chars_removed}")
        print(f"- File saved: {file_path}")

        return True

    except Exception as e:
        print(f"Error cleaning file: {e}")
        return False

def main():
    # Default path
    default_path = Path("../data/keywords.json").resolve()

    if default_path.exists():
        print("NextBuild Keywords Content Cleaner")
        print("==================================")
        print()

        # First analyze
        data = analyze_keywords_file(str(default_path))
        if data is None:
            return

        print()
        response = input("Would you like to clean the file? (y/n): ").lower().strip()

        if response in ['y', 'yes']:
            print()
            clean_keywords_file(str(default_path))
        else:
            print("Cleaning cancelled.")

    else:
        print(f"Keywords file not found: {default_path}")
        print("Please run this script from the scripts directory.")

if __name__ == "__main__":
    main()







