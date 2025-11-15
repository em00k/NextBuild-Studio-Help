#!/usr/bin/env python3
"""
Extract functions and subroutines from BASIC files and generate markdown documentation.
"""

import sys
from pathlib import Path


def extract_functions_and_subs(file_path):
    """
    Extract all function and subroutine declarations from a BASIC file.
    
    Args:
        file_path: Path to the BASIC file
        
    Returns:
        tuple: (subroutines list, functions list)
    """
    subroutines = []
    functions = []
    
    # Pattern to match BASIC function/sub declarations
    # Matches: Sub/Function [fastcall] Name(...) [as Type]
    # Excludes: assembly instructions like "sub h", "sub l", "sub c", "sub 32", etc.
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                stripped = line.strip()
                # Skip empty lines
                if not stripped:
                    continue
                
                stripped_lower = stripped.lower()
                
                # Check for subroutine declarations
                if stripped_lower.startswith('sub '):
                    parts = stripped.split(None, 3)  # Split into max 4 parts
                    if len(parts) >= 2:
                        second_part = parts[1].lower()
                        # Exclude assembly instructions: single char/number after "sub "
                        # Also exclude pure numeric tokens (like "32", "34")
                        if (len(second_part) == 1 and second_part in 'hlc0123456789') or second_part.isdigit():
                            continue
                        # If second part is "fastcall", check third part
                        if second_part == 'fastcall' and len(parts) >= 3:
                            third_part = parts[2]
                            if (len(third_part) == 1 and third_part.lower() in 'hlc0123456789') or third_part.isdigit():
                                continue
                        # Valid sub declaration
                        subroutines.append(stripped)
                
                # Check for function declarations
                elif stripped_lower.startswith('function '):
                    parts = stripped.split(None, 3)
                    if len(parts) >= 2:
                        second_part = parts[1].lower()
                        # Exclude single character/number (assembly)
                        # Also exclude pure numeric tokens
                        if (len(second_part) == 1 and second_part in 'hlc0123456789') or second_part.isdigit():
                            continue
                        # If second part is "fastcall", check third part
                        if second_part == 'fastcall' and len(parts) >= 3:
                            third_part = parts[2]
                            if (len(third_part) == 1 and third_part.lower() in 'hlc0123456789') or third_part.isdigit():
                                continue
                        # Valid function declaration
                        functions.append(stripped)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    
    return subroutines, functions


def generate_markdown(file_path, subroutines, functions, output_path=None):
    """
    Generate markdown documentation from extracted functions and subroutines.
    
    Args:
        file_path: Original file path
        subroutines: List of subroutine declarations
        functions: List of function declarations
        output_path: Optional output path (defaults to input filename with .md extension)
    """
    file_path_obj = Path(file_path)
    file_name = file_path_obj.name
    
    # Get relative path if possible, otherwise use absolute path
    try:
        relative_path = file_path_obj.relative_to(Path.cwd())
    except ValueError:
        relative_path = file_path_obj
    
    total = len(subroutines) + len(functions)
    
    # Determine output path
    if output_path is None:
        output_path = file_path_obj.with_suffix('.md')
    else:
        output_path = Path(output_path)
    
    # Generate markdown content
    md_content = f"## {file_name}\n"
    md_content += f"## {relative_path}\n\n"
    md_content += f"- Sub Routines : {len(subroutines)}\n"
    md_content += f"- Functions       : {len(functions)}\n\n"
    
    # Add all subroutines
    for sub in subroutines:
        md_content += f"{sub}\n"
    
    # Add all functions
    for func in functions:
        md_content += f"{func}\n"
    
    # Write to file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"Successfully generated: {output_path}")
        print(f"  - Subroutines: {len(subroutines)}")
        print(f"  - Functions: {len(functions)}")
        print(f"  - Total: {total}")
    except Exception as e:
        print(f"Error writing output file: {e}")
        sys.exit(1)


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python extract_functions.py <input_file> [output_file]")
        print("Example: python extract_functions.py nextlib.bas")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    # Extract functions and subroutines
    subroutines, functions = extract_functions_and_subs(input_file)
    
    # Generate markdown
    generate_markdown(input_file, subroutines, functions, output_file)


if __name__ == '__main__':
    main()

