#!/usr/bin/env python3
"""
NextBuild Snippets Editor GUI
A Python GUI application for editing NextBuild JSON snippet files

Usage:
    python nextbuild_snippet_editor.py [filename.json]

If no filename is provided, attempts to auto-load ../snippets/nextbuild.json
"""

import json
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os
import sys
from pathlib import Path


class SnippetEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("NextBuild Snippets Editor")
        self.root.geometry("1200x800")

        # Initialize variables
        self.snippets_data = {}
        self.current_snippet_key = None
        self.snippet_keys = []
        self.current_index = 0
        self.file_path = None

        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(1, weight=1)

        # Create menu bar
        self.create_menu()

        # Create toolbar
        self.create_toolbar()

        # Create left panel (snippet list)
        self.create_snippet_list()

        # Create right panel (editor)
        self.create_editor_panel()

        # Create status bar
        self.create_status_bar()

        # Bind keyboard shortcuts
        self.root.bind('<Control-s>', lambda e: self.save_file())
        self.root.bind('<Control-o>', lambda e: self.open_file())
        self.root.bind('<Control-n>', lambda e: self.new_snippet())
        self.root.bind('<Delete>', lambda e: self.delete_snippet_and_refocus())
        self.root.bind('<KP_Delete>', lambda e: self.delete_snippet_and_refocus())  # Numeric keypad delete

        # Auto-load snippets file from command line or default location
        file_to_load = None

        # Check for command line argument
        if len(sys.argv) > 1:
            file_to_load = sys.argv[1]
        else:
            # Fall back to default location
            default_path = Path("../snippets/nextbuild.json").resolve()
            if default_path.exists():
                file_to_load = str(default_path)

        if file_to_load:
            self.load_file(file_to_load)

    def create_menu(self):
        """Create the menu bar"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open...", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As...", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="New Snippet", command=self.new_snippet, accelerator="Ctrl+N")
        edit_menu.add_command(label="Delete Snippet", command=self.delete_snippet)
        edit_menu.add_separator()
        edit_menu.add_command(label="Duplicate Snippet", command=self.duplicate_snippet)

        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    def create_toolbar(self):
        """Create the toolbar"""
        toolbar = ttk.Frame(self.main_frame)
        toolbar.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))

        # File operations
        ttk.Button(toolbar, text="Open", command=self.open_file).grid(row=0, column=0, padx=2)
        ttk.Button(toolbar, text="Save", command=self.save_file).grid(row=0, column=1, padx=2)

        ttk.Separator(toolbar, orient=tk.VERTICAL).grid(row=0, column=2, sticky=(tk.N, tk.S), padx=5)

        # Snippet operations
        ttk.Button(toolbar, text="New", command=self.new_snippet).grid(row=0, column=3, padx=2)
        ttk.Button(toolbar, text="Delete", command=self.delete_snippet).grid(row=0, column=4, padx=2)
        ttk.Button(toolbar, text="Duplicate", command=self.duplicate_snippet).grid(row=0, column=5, padx=2)

        ttk.Separator(toolbar, orient=tk.VERTICAL).grid(row=0, column=6, sticky=(tk.N, tk.S), padx=5)

        # Navigation
        ttk.Button(toolbar, text="◀ Prev", command=self.prev_snippet).grid(row=0, column=7, padx=2)
        ttk.Button(toolbar, text="Next ▶", command=self.next_snippet).grid(row=0, column=8, padx=2)

    def create_snippet_list(self):
        """Create the snippet list panel"""
        # Left panel frame
        left_frame = ttk.LabelFrame(self.main_frame, text="Snippets", padding="5")
        left_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 5))

        # Search frame
        search_frame = ttk.Frame(left_frame)
        search_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 5))

        ttk.Label(search_frame, text="Search:").grid(row=0, column=0, sticky=tk.W)
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        self.search_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(5, 0))
        self.search_entry.bind('<KeyRelease>', self.filter_snippets)

        search_frame.columnconfigure(1, weight=1)

        # Snippets list
        list_frame = ttk.Frame(left_frame)
        list_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Create Treeview for snippets
        self.snippet_tree = ttk.Treeview(list_frame, columns=("prefix",), show="tree headings", height=20)
        self.snippet_tree.heading("#0", text="Snippet Name")
        self.snippet_tree.heading("prefix", text="Prefix")
        self.snippet_tree.column("#0", width=200)
        self.snippet_tree.column("prefix", width=100)

        # Scrollbars for tree
        tree_scroll_y = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.snippet_tree.yview)
        tree_scroll_x = ttk.Scrollbar(list_frame, orient=tk.HORIZONTAL, command=self.snippet_tree.xview)
        self.snippet_tree.configure(yscrollcommand=tree_scroll_y.set, xscrollcommand=tree_scroll_x.set)

        self.snippet_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        tree_scroll_y.grid(row=0, column=1, sticky=(tk.N, tk.S))
        tree_scroll_x.grid(row=1, column=0, sticky=(tk.W, tk.E))

        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)

        # Bind selection event
        self.snippet_tree.bind('<<TreeviewSelect>>', self.on_snippet_select)

        left_frame.columnconfigure(0, weight=1)
        left_frame.rowconfigure(1, weight=1)

    def create_editor_panel(self):
        """Create the editor panel"""
        # Right panel frame
        right_frame = ttk.LabelFrame(self.main_frame, text="Editor", padding="5")
        right_frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Snippet info frame
        info_frame = ttk.Frame(right_frame)
        info_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))

        ttk.Label(info_frame, text="Snippet Name:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.name_var = tk.StringVar()
        self.name_entry = ttk.Entry(info_frame, textvariable=self.name_var, width=50)
        self.name_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(5, 0), pady=2)
        self.name_entry.bind('<KeyRelease>', self.on_name_change)

        ttk.Label(info_frame, text="Prefix:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.prefix_var = tk.StringVar()
        self.prefix_entry = ttk.Entry(info_frame, textvariable=self.prefix_var)
        self.prefix_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(5, 0), pady=2)

        info_frame.columnconfigure(1, weight=1)

        # Body editor
        body_frame = ttk.LabelFrame(right_frame, text="Body (one line per array element)", padding="5")
        body_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))

        self.body_text = scrolledtext.ScrolledText(body_frame, height=15, wrap=tk.NONE)
        self.body_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Description editor
        desc_frame = ttk.LabelFrame(right_frame, text="Description", padding="5")
        desc_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.desc_text = scrolledtext.ScrolledText(desc_frame, height=8)
        self.desc_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Bind change events
        self.prefix_entry.bind('<KeyRelease>', self.on_field_change)
        self.body_text.bind('<KeyRelease>', self.on_field_change)
        self.desc_text.bind('<KeyRelease>', self.on_field_change)

        right_frame.columnconfigure(0, weight=1)
        right_frame.rowconfigure(1, weight=1)
        right_frame.rowconfigure(2, weight=1)

    def create_status_bar(self):
        """Create the status bar"""
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(self.main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))

    def open_file(self):
        """Open a JSON file"""
        file_path = filedialog.askopenfilename(
            title="Open Snippets File",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            initialdir="../snippets"
        )
        if file_path:
            self.load_file(file_path)

    def load_file(self, file_path):
        """Load snippets from JSON file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                self.snippets_data = json.load(f)

            self.file_path = file_path
            self.snippet_keys = list(self.snippets_data.keys())
            self.current_index = 0
            self.current_snippet_key = self.snippet_keys[0] if self.snippet_keys else None

            self.update_snippet_list()
            if self.current_snippet_key:
                self.display_snippet(self.current_snippet_key)

            self.status_var.set(f"Loaded {len(self.snippet_keys)} snippets from {os.path.basename(file_path)}")
            self.root.title(f"NextBuild Snippets Editor - {os.path.basename(file_path)}")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {str(e)}")

    def save_file(self):
        """Save snippets to JSON file"""
        if not self.file_path:
            return self.save_file_as()

        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(self.snippets_data, f, indent=2, ensure_ascii=False)

            self.status_var.set(f"Saved {len(self.snippet_keys)} snippets to {os.path.basename(self.file_path)}")
            messagebox.showinfo("Success", "File saved successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {str(e)}")

    def save_file_as(self):
        """Save snippets to a new JSON file"""
        file_path = filedialog.asksaveasfilename(
            title="Save Snippets File As",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            initialdir="../snippets",
            defaultextension=".json"
        )
        if file_path:
            self.file_path = file_path
            self.save_file()

    def update_snippet_list(self):
        """Update the snippet list in the treeview"""
        # Clear existing items
        for item in self.snippet_tree.get_children():
            self.snippet_tree.delete(item)

        # Filter snippets based on search
        search_term = self.search_var.get().lower()
        filtered_keys = [key for key in self.snippet_keys if search_term in key.lower()]

        # Add filtered snippets to tree
        for key in filtered_keys:
            snippet = self.snippets_data[key]
            prefix = snippet.get('prefix', '')
            self.snippet_tree.insert('', tk.END, text=key, values=(prefix,))

    def filter_snippets(self, event=None):
        """Filter snippets based on search term"""
        self.update_snippet_list()

    def on_snippet_select(self, event):
        """Handle snippet selection in the treeview"""
        selection = self.snippet_tree.selection()
        if selection:
            item = selection[0]
            snippet_name = self.snippet_tree.item(item, 'text')
            if snippet_name in self.snippets_data:
                self.current_snippet_key = snippet_name
                self.current_index = self.snippet_keys.index(snippet_name)
                self.display_snippet(snippet_name)

    def display_snippet(self, snippet_key):
        """Display a snippet in the editor"""
        if snippet_key not in self.snippets_data:
            return

        snippet = self.snippets_data[snippet_key]

        # Update fields
        self.name_var.set(snippet_key)
        self.prefix_var.set(snippet.get('prefix', ''))

        # Update body text
        body_lines = snippet.get('body', [])
        if isinstance(body_lines, list):
            self.body_text.delete(1.0, tk.END)
            self.body_text.insert(1.0, '\n'.join(body_lines))
        else:
            self.body_text.delete(1.0, tk.END)
            self.body_text.insert(1.0, str(body_lines))

        # Update description
        self.desc_text.delete(1.0, tk.END)
        self.desc_text.insert(1.0, snippet.get('description', ''))

        self.status_var.set(f"Editing: {snippet_key}")

    def on_name_change(self, event=None):
        """Handle snippet name change"""
        new_name = self.name_var.get().strip()
        if new_name and new_name != self.current_snippet_key:
            # Check if name already exists
            if new_name in self.snippets_data and new_name != self.current_snippet_key:
                messagebox.showwarning("Warning", "A snippet with this name already exists!")
                self.name_var.set(self.current_snippet_key)
                return

            # Rename the snippet
            if self.current_snippet_key in self.snippets_data:
                self.snippets_data[new_name] = self.snippets_data.pop(self.current_snippet_key)
                self.snippet_keys[self.current_index] = new_name
                self.current_snippet_key = new_name
                self.update_snippet_list()
                self.status_var.set(f"Renamed to: {new_name}")

    def on_field_change(self, event=None):
        """Handle field changes"""
        if not self.current_snippet_key:
            return

        # Update the snippet data
        self.snippets_data[self.current_snippet_key]['prefix'] = self.prefix_var.get()

        # Update body
        body_text = self.body_text.get(1.0, tk.END).strip()
        self.snippets_data[self.current_snippet_key]['body'] = body_text.split('\n') if body_text else []

        # Update description
        self.snippets_data[self.current_snippet_key]['description'] = self.desc_text.get(1.0, tk.END).strip()

    def new_snippet(self):
        """Create a new snippet"""
        # Find a unique name
        base_name = "New Snippet"
        counter = 1
        new_name = base_name
        while new_name in self.snippets_data:
            new_name = f"{base_name} {counter}"
            counter += 1

        # Create new snippet
        self.snippets_data[new_name] = {
            "prefix": "",
            "body": [""],
            "description": ""
        }

        self.snippet_keys.append(new_name)
        self.current_index = len(self.snippet_keys) - 1
        self.current_snippet_key = new_name

        self.update_snippet_list()
        self.display_snippet(new_name)

        # Select the new item in the tree
        for item in self.snippet_tree.get_children():
            if self.snippet_tree.item(item, 'text') == new_name:
                self.snippet_tree.selection_set(item)
                self.snippet_tree.focus(item)
                break

    def delete_snippet(self):
        """Delete the current snippet"""
        if not self.current_snippet_key:
            return

        if messagebox.askyesno("Confirm Delete", f"Delete snippet '{self.current_snippet_key}'?"):
            del self.snippets_data[self.current_snippet_key]
            self.snippet_keys.remove(self.current_snippet_key)

            if self.snippet_keys:
                self.current_index = max(0, self.current_index - 1)
                self.current_snippet_key = self.snippet_keys[self.current_index]
                self.display_snippet(self.current_snippet_key)
            else:
                self.current_snippet_key = None
                self.clear_editor()

            self.update_snippet_list()
            self.status_var.set(f"Deleted: {self.current_snippet_key}")

    def delete_snippet_and_refocus(self):
        """Delete the current snippet and refocus on the list for rapid editing"""
        self.delete_snippet()
        # Focus back on the snippet list for rapid editing
        self.snippet_tree.focus()
        # Select the current item in the tree if there are items left
        if self.snippet_keys and self.current_snippet_key:
            self.select_current_in_tree()

    def duplicate_snippet(self):
        """Duplicate the current snippet"""
        if not self.current_snippet_key:
            return

        # Find a unique name
        base_name = f"{self.current_snippet_key} Copy"
        counter = 1
        new_name = base_name
        while new_name in self.snippets_data:
            new_name = f"{base_name} {counter}"
            counter += 1

        # Duplicate the snippet
        self.snippets_data[new_name] = self.snippets_data[self.current_snippet_key].copy()

        self.snippet_keys.append(new_name)
        self.current_index = len(self.snippet_keys) - 1
        self.current_snippet_key = new_name

        self.update_snippet_list()
        self.display_snippet(new_name)

    def prev_snippet(self):
        """Navigate to previous snippet"""
        if self.snippet_keys and self.current_index > 0:
            self.current_index -= 1
            self.current_snippet_key = self.snippet_keys[self.current_index]
            self.display_snippet(self.current_snippet_key)

            # Update tree selection
            self.select_current_in_tree()

    def next_snippet(self):
        """Navigate to next snippet"""
        if self.snippet_keys and self.current_index < len(self.snippet_keys) - 1:
            self.current_index += 1
            self.current_snippet_key = self.snippet_keys[self.current_index]
            self.display_snippet(self.current_snippet_key)

            # Update tree selection
            self.select_current_in_tree()

    def select_current_in_tree(self):
        """Select the current snippet in the treeview"""
        for item in self.snippet_tree.get_children():
            if self.snippet_tree.item(item, 'text') == self.current_snippet_key:
                self.snippet_tree.selection_set(item)
                self.snippet_tree.focus(item)
                self.snippet_tree.see(item)
                break

    def clear_editor(self):
        """Clear all editor fields"""
        self.name_var.set("")
        self.prefix_var.set("")
        self.body_text.delete(1.0, tk.END)
        self.desc_text.delete(1.0, tk.END)

    def show_about(self):
        """Show about dialog"""
        messagebox.showinfo("About", "NextBuild Snippets Editor\n\nA GUI tool for editing NextBuild JSON snippet files.\n\nFeatures:\n• Load and save JSON snippet files\n• Edit snippet properties\n• Navigate between snippets\n• Search and filter snippets\n• Create, duplicate, and delete snippets")


def main():
    root = tk.Tk()
    app = SnippetEditor(root)
    root.mainloop()


if __name__ == "__main__":
    main()





