import os
import json

def convert_md_folder_to_json(md_folder, output_json):
    """
    Recursively reads all .md files in `md_folder`, maps each file's uppercase basename (without extension)
    to an object with 'content' and 'category' (immediate parent folder), and writes the result as JSON.
    """
    mapping = {}
    for root, dirs, files in os.walk(md_folder):
        for filename in files:
            if filename.lower().endswith('.md'):
                key = os.path.splitext(filename)[0].upper()
                file_path = os.path.join(root, filename)
                category = os.path.basename(os.path.dirname(file_path))
                with open(file_path, 'r', encoding='utf-8') as f:
                    mapping[key] = {
                        "content": f.read(),
                        "category": category
                    }
    with open(output_json, 'w', encoding='utf-8') as out:
        json.dump(mapping, out, indent=4, ensure_ascii=False)
    print(f'Processed {len(mapping)} files. Output written to {output_json}')

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Convert a folder of .md files into a JSON mapping with categories')
    parser.add_argument('md_folder', help='Path to the folder containing .md files')
    parser.add_argument('output_json', help='Path for the output JSON file')
    args = parser.parse_args()
    convert_md_folder_to_json(args.md_folder, args.output_json)