import tkinter as tk
from tkinter import messagebox, filedialog
import os
import re

class MarkdownBoilerplateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MD Boilerplate Generator")

        # State for file browsing
        self.folder_path = None
        self.file_list = []
        self.current_index = -1

        # Keyword
        tk.Label(root, text="Keyword:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.keyword_entry = tk.Entry(root)
        self.keyword_entry.grid(row=0, column=1, columnspan=3, sticky="we", padx=5, pady=5)

        # Syntax
        tk.Label(root, text="Syntax:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.syntax_entry = tk.Entry(root)
        self.syntax_entry.grid(row=1, column=1, columnspan=3, sticky="we", padx=5, pady=5)

        # Description
        tk.Label(root, text="Description:").grid(row=2, column=0, sticky="ne", padx=5, pady=5)
        self.description_text = tk.Text(root, height=5)
        self.description_text.grid(row=2, column=1, columnspan=3, sticky="we", padx=5, pady=5)

        # Examples
        tk.Label(root, text="Examples:").grid(row=3, column=0, sticky="ne", padx=5, pady=5)
        self.examples_text = tk.Text(root, height=5)
        self.examples_text.grid(row=3, column=1, columnspan=3, sticky="we", padx=5, pady=5)

        # Remarks
        tk.Label(root, text="Remarks:").grid(row=4, column=0, sticky="ne", padx=5, pady=5)
        self.links_text = tk.Text(root, height=3)
        self.links_text.grid(row=4, column=1, columnspan=3, sticky="we", padx=5, pady=5)

        # Buttons
        self.load_button = tk.Button(root, text="Load Folder", command=self.load_folder)
        self.load_button.grid(row=5, column=0, pady=10, padx=5)

        self.save_button = tk.Button(root, text="Save", command=self.save_markdown)
        self.save_button.grid(row=5, column=1, pady=10)

        self.clear_button = tk.Button(root, text="Clear", command=self.clear_fields)
        self.clear_button.grid(row=5, column=2, pady=10)

        self.prev_button = tk.Button(root, text="<< Prev", command=self.prev_file, state=tk.DISABLED)
        self.prev_button.grid(row=5, column=3, pady=10, padx=5)

        self.next_button = tk.Button(root, text="Next >>", command=self.next_file, state=tk.DISABLED)
        self.next_button.grid(row=5, column=4, pady=10, padx=5)

        # Configure column resizing
        for i in range(5):
            root.columnconfigure(i, weight=1)

        # Set initial focus
        self.keyword_entry.focus_set()

    def save_markdown(self):
        keyword = self.keyword_entry.get().strip()
        if not keyword:
            messagebox.showerror("Error", "Keyword cannot be empty.")
            self.keyword_entry.focus_set()
            return

        syntax = self.syntax_entry.get().strip()
        description = self.description_text.get("1.0", tk.END).strip()
        examples = self.examples_text.get("1.0", tk.END).strip()
        links = self.links_text.get("1.0", tk.END).strip()

        md_content = f"""# {keyword}

## Syntax

```
{syntax}
```

## Description

{description}

**Examples**

{examples}

## Links

{links}
"""

        filename = f"{keyword}.md"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(md_content)
            messagebox.showinfo("Saved", f"Markdown saved as {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {e}")

    def clear_fields(self):
        self.keyword_entry.delete(0, tk.END)
        self.syntax_entry.delete(0, tk.END)
        self.description_text.delete("1.0", tk.END)
        self.examples_text.delete("1.0", tk.END)
        self.links_text.delete("1.0", tk.END)
        self.keyword_entry.focus_set()

    def load_folder(self):
        folder = filedialog.askdirectory()
        if not folder:
            return
        md_files = sorted([f for f in os.listdir(folder) if f.lower().endswith('.md')])
        if not md_files:
            messagebox.showerror("Error", "No markdown files found in selected folder.")
            return
        self.folder_path = folder
        self.file_list = md_files
        self.current_index = 0
        self.load_current_file()
        self.update_nav_buttons()

    def load_current_file(self):
        filepath = os.path.join(self.folder_path, self.file_list[self.current_index])
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()

            # Clear fields first
            self.clear_fields()

            # Keyword
            kw_match = re.search(r'^#\s*(.+)', text, re.MULTILINE)
            if kw_match:
                self.keyword_entry.insert(0, kw_match.group(1).strip())

            # Syntax
            syntax_match = re.search(r'##\s*Syntax\s*```[\s\S]*?```', text)
            if syntax_match:
                code_block = re.search(r'```[\r\n]+([\s\S]*?)```', syntax_match.group(0))
                if code_block:
                    self.syntax_entry.insert(0, code_block.group(1).strip())

            # Description
            desc_match = re.search(r'##\s*Description\s*([\s\S]*?)(?=\n##\s|\Z)', text)
            if desc_match:
                self.description_text.insert('1.0', desc_match.group(1).strip())

            # Examples
            ex_match = re.search(r'\*\*Examples\*\*\s*([\s\S]*?)(?=\n##\s|\Z)', text)
            if ex_match:
                self.examples_text.insert('1.0', ex_match.group(1).strip())

            # Links/Remarks
            link_match = re.search(r'##\s*Links\s*([\s\S]*?)(?=\n##\s|\Z)', text)
            if link_match:
                self.links_text.insert('1.0', link_match.group(1).strip())

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {e}")

    def update_nav_buttons(self):
        if self.file_list:
            self.prev_button.config(state=tk.NORMAL if self.current_index > 0 else tk.DISABLED)
            self.next_button.config(state=tk.NORMAL if self.current_index < len(self.file_list)-1 else tk.DISABLED)

    def prev_file(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.load_current_file()
            self.update_nav_buttons()

    def next_file(self):
        if self.current_index < len(self.file_list) - 1:
            self.current_index += 1
            self.load_current_file()
            self.update_nav_buttons()

if __name__ == "__main__":
    root = tk.Tk()
    app = MarkdownBoilerplateApp(root)
    root.mainloop()
