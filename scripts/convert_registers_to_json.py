#!/usr/bin/env python3
"""
Convert registers.md to JSON format for nextbuild_constants.json
Parses the markdown table and extracts register information
"""

import json
import re
from pathlib import Path


def parse_registers_md(md_file_path):
    """Parse registers.md and extract register information"""
    registers = {}

    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match table rows like:
    # | $00 | [MACHINE_ID_NR_00](MACHINE_ID_NR_00.md) - Identifies TBBlue board type...
    pattern = r'\|\s*\$([0-9A-Fa-f]+)\s*\|\s*\[([A-Z0-9_]+)\]\([^)]+\)\s*-\s*(.+?)\s*\|'

    matches = re.findall(pattern, content)

    for hex_value, register_name, description in matches:
        # Convert hex to decimal
        decimal_value = int(hex_value, 16)

        # Clean up description (remove markdown links, extra whitespace)
        clean_description = description.strip()

        registers[register_name] = {
            "value": decimal_value,
            "description": clean_description
        }

    return registers


def main():
    # Paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    md_file = project_root / "docs" / "registers.md"
    json_file = project_root / "jsonfiles" / "nextbuild_constants.json"
    output_file = project_root / "jsonfiles" / "registers_converted.json"

    print(f"Reading registers from: {md_file}")

    # Parse registers
    registers = parse_registers_md(md_file)

    print(f"Found {len(registers)} registers")

    # Read existing constants if they exist
    existing_constants = {}
    if json_file.exists():
        with open(json_file, 'r', encoding='utf-8') as f:
            existing_constants = json.load(f)
        print(f"Loaded {len(existing_constants)} existing constants")

    # Option 1: Save just the registers to a new file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(registers, f, indent=2, ensure_ascii=False)
    print(f"\nSaved registers to: {output_file}")

    # Option 2: Merge with existing constants
    merged = {**existing_constants, **registers}
    merged_file = project_root / "jsonfiles" / "nextbuild_constants_merged.json"
    with open(merged_file, 'w', encoding='utf-8') as f:
        json.dump(merged, f, indent=2, ensure_ascii=False)
    print(f"Saved merged constants to: {merged_file}")

    # Show some examples
    print("\nExample conversions:")
    for i, (name, data) in enumerate(list(registers.items())[:5]):
        print(f'  "{name}": {{')
        print(f'    "value": {data["value"]},')
        print(f'    "description": "{data["description"]}"')
        print(f'  }}')
        if i < 4:
            print()


if __name__ == "__main__":
    main()
