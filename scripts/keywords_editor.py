#!/usr/bin/env python3
"""
NextBuild Keywords Editor GUI
A Python GUI application for editing NextBuild keywords JSON files

Usage:
    python keywords_editor.py [filename.json]

If no filename is provided, attempts to auto-load ../data/keywords.json
"""

import json
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os
import re
import sys
from pathlib import Path
import markdown
from tkhtmlview import HTMLScrolledText


class KeywordsEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("NextBuild Keywords Editor")
        self.root.geometry("1400x900")

        # Initialize variables
        self.keywords_data = {}
        self.current_keyword_key = None
        self.keyword_keys = []
        self.current_index = 0
        self.file_path = None
        self.search_var = tk.StringVar()
        self.category_filter = tk.StringVar(value="All")

        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(2, weight=1)

        # Create menu bar
        self.create_menu()

        # Create toolbar
        self.create_toolbar()

        # Create search and filter bar
        self.create_search_filter()

        # Create left panel (keywords list)
        self.create_keywords_list()

        # Create right panel (editor)
        self.create_editor_panel()

        # Create status bar
        self.create_status_bar()

        # Bind keyboard shortcuts
        self.root.bind('<Control-s>', lambda e: self.save_file())
        self.root.bind('<Control-o>', lambda e: self.open_file())
        self.root.bind('<Control-n>', lambda e: self.new_keyword())
        self.root.bind('<Control-d>', lambda e: self.duplicate_keyword())
        self.root.bind('<Delete>', lambda e: self.delete_keyword())

        # Auto-load keywords file from command line or default location
        file_to_load = None

        # Check for command line argument
        if len(sys.argv) > 1:
            file_to_load = sys.argv[1]
        else:
            # Fall back to default location
            default_path = Path("../data/keywords.json").resolve()
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
        edit_menu.add_command(label="New Keyword", command=self.new_keyword, accelerator="Ctrl+N")
        edit_menu.add_command(label="Delete Keyword", command=self.delete_keyword, accelerator="Del")
        edit_menu.add_separator()
        edit_menu.add_command(label="Duplicate Keyword", command=self.duplicate_keyword, accelerator="Ctrl+D")

        # View menu
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="View", menu=view_menu)
        view_menu.add_command(label="Sort by Name", command=self.sort_by_name)
        view_menu.add_command(label="Sort by Category", command=self.sort_by_category)

        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    def create_toolbar(self):
        """Create the toolbar"""
        toolbar = ttk.Frame(self.main_frame)
        toolbar.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 5))

        # File operations
        ttk.Button(toolbar, text="Open", command=self.open_file).grid(row=0, column=0, padx=2)
        ttk.Button(toolbar, text="Save", command=self.save_file).grid(row=0, column=1, padx=2)

        ttk.Separator(toolbar, orient=tk.VERTICAL).grid(row=0, column=2, sticky=(tk.N, tk.S), padx=5)

        # Keyword operations
        ttk.Button(toolbar, text="New", command=self.new_keyword).grid(row=0, column=3, padx=2)
        ttk.Button(toolbar, text="Delete", command=self.delete_keyword).grid(row=0, column=4, padx=2)
        ttk.Button(toolbar, text="Duplicate", command=self.duplicate_keyword).grid(row=0, column=5, padx=2)

    def create_search_filter(self):
        """Create search and filter controls"""
        search_frame = ttk.Frame(self.main_frame)
        search_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))

        # Search
        ttk.Label(search_frame, text="Search:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        search_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        search_entry.bind('<KeyRelease>', self.on_search_change)

        # Category filter
        ttk.Label(search_frame, text="Category:").grid(row=0, column=2, sticky=tk.W, padx=(0, 5))
        category_combo = ttk.Combobox(search_frame, textvariable=self.category_filter,
                                    values=["All", "keywords", "manual", "esxdos", "nextlib", "constants"],
                                    state="readonly", width=15)
        category_combo.grid(row=0, column=3, sticky=tk.W, padx=(0, 10))
        category_combo.bind('<<ComboboxSelected>>', self.on_filter_change)

        # Configure grid weights
        search_frame.columnconfigure(1, weight=1)

    def create_keywords_list(self):
        """Create the keywords list panel"""
        # Left panel frame
        left_frame = ttk.LabelFrame(self.main_frame, text="Keywords", padding="5")
        left_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 10))

        # Create listbox with scrollbar
        list_frame = ttk.Frame(left_frame)
        list_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

        # Listbox
        self.keywords_listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set,
                                         selectmode=tk.SINGLE, exportselection=False)
        self.keywords_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.config(command=self.keywords_listbox.yview)

        # Bind selection event
        self.keywords_listbox.bind('<<ListboxSelect>>', self.on_keyword_select)

        # Configure grid weights
        left_frame.columnconfigure(0, weight=1)
        left_frame.rowconfigure(0, weight=1)
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)

    def create_editor_panel(self):
        """Create the editor panel"""
        # Right panel frame
        right_frame = ttk.LabelFrame(self.main_frame, text="Keyword Editor", padding="5")
        right_frame.grid(row=2, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configure grid weights
        right_frame.columnconfigure(0, weight=1)
        right_frame.rowconfigure(2, weight=1)

        # Keyword name
        ttk.Label(right_frame, text="Keyword:").grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        self.keyword_entry = ttk.Entry(right_frame)
        self.keyword_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=(0, 5))
        self.keyword_entry.bind('<KeyRelease>', self.on_keyword_name_change)

        # Category
        ttk.Label(right_frame, text="Category:").grid(row=1, column=0, sticky=tk.W, pady=(0, 5))
        self.category_entry = ttk.Combobox(right_frame, values=["keywords", "manual", "esxdos", "nextlib", "constants"])
        self.category_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=(0, 5))
        self.category_entry.bind('<KeyRelease>', self.on_category_change)
        self.category_entry.bind('<<ComboboxSelected>>', self.on_category_change)

        # Checkboxes frame
        checkboxes_frame = ttk.Frame(right_frame)
        checkboxes_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))

        self.show_in_list_var = tk.BooleanVar()
        ttk.Checkbutton(checkboxes_frame, text="Show in Keyword List",
                       variable=self.show_in_list_var, command=self.on_show_in_list_change).grid(row=0, column=0, sticky=tk.W)

        self.manual_only_var = tk.BooleanVar()
        ttk.Checkbutton(checkboxes_frame, text="Manual Only",
                       variable=self.manual_only_var, command=self.on_manual_only_change).grid(row=0, column=1, sticky=tk.W)

        # Content tools
        content_tools_frame = ttk.Frame(right_frame)
        content_tools_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 5))

        ttk.Button(content_tools_frame, text="Clean Content", command=self.clean_content).grid(row=0, column=0, padx=(0, 5))
        ttk.Button(content_tools_frame, text="Format Markdown", command=self.format_markdown).grid(row=0, column=1, padx=(0, 5))

        # Content tabs
        self.content_notebook = ttk.Notebook(right_frame)
        self.content_notebook.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Edit tab
        edit_frame = ttk.Frame(self.content_notebook)
        self.content_notebook.add(edit_frame, text="Edit")

        self.content_text = scrolledtext.ScrolledText(edit_frame, wrap=tk.WORD, height=20,
                                                     font=("Consolas", 10))
        self.content_text.pack(fill=tk.BOTH, expand=True)
        self.content_text.bind('<KeyRelease>', self.on_content_change)

        # Create context menu for keyword links
        self.context_menu = None
        self.keywords_submenu = None

        # Preview tab
        preview_frame = ttk.Frame(self.content_notebook)
        self.content_notebook.add(preview_frame, text="Preview")

        preview_tools = ttk.Frame(preview_frame)
        preview_tools.pack(fill=tk.X, pady=(0, 5))

        ttk.Button(preview_tools, text="Refresh Preview", command=self.update_preview).pack(side=tk.LEFT)

        # Use HTMLScrolledText for proper markdown rendering
        self.preview_text = HTMLScrolledText(preview_frame, html="<p>Preview will appear here</p>")
        self.preview_text.pack(fill=tk.BOTH, expand=True)

        # Configure grid weights
        right_frame.columnconfigure(1, weight=1)
        right_frame.rowconfigure(4, weight=1)

        # Create context menu after all widgets are initialized
        self.create_context_menu()

    def create_context_menu(self):
        """Create context menu for keyword links"""
        self.context_menu = tk.Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="Insert Keyword Link", command=self.show_keyword_dialog)

        # Bind right-click to content text
        self.content_text.bind("<Button-3>", self.show_context_menu)

        # Bind Ctrl+K for quick keyword linking
        self.content_text.bind("<Control-k>", lambda e: self.show_keyword_dialog())

    def show_context_menu(self, event):
        """Show context menu at cursor position"""
        if not self.current_keyword_key:
            return

        # Show the menu
        try:
            self.context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.context_menu.grab_release()

    def show_keyword_dialog(self):
        """Show keyword selection dialog"""
        if not self.current_keyword_key:
            return

        # Create dialog window
        dialog = tk.Toplevel(self.root)
        dialog.title("Insert Keyword Link")
        dialog.geometry("400x500")
        dialog.resizable(True, True)
        dialog.transient(self.root)
        dialog.grab_set()

        # Center the dialog
        dialog.geometry("+{}+{}".format(
            self.root.winfo_rootx() + 50,
            self.root.winfo_rooty() + 50
        ))

        # Create main frame
        main_frame = ttk.Frame(dialog, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Search frame
        search_frame = ttk.Frame(main_frame)
        search_frame.pack(fill=tk.X, pady=(0, 10))

        ttk.Label(search_frame, text="Search:").pack(side=tk.LEFT)
        search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=search_var)
        search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 0))

        # Status label for count
        count_label = ttk.Label(search_frame, text="")
        count_label.pack(side=tk.RIGHT, padx=(5, 0))

        # Keywords list frame
        list_frame = ttk.Frame(main_frame)
        list_frame.pack(fill=tk.BOTH, expand=True)

        # Create listbox with scrollbar
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        keywords_listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set,
                                    selectmode=tk.SINGLE, exportselection=False,
                                    font=("Consolas", 10))
        keywords_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=keywords_listbox.yview)

        # Populate listbox with keywords (excluding current)
        available_keywords = [k for k in sorted(self.keyword_keys) if k != self.current_keyword_key]
        for keyword in available_keywords:
            keywords_listbox.insert(tk.END, keyword)

        # Button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=(10, 0))

        def insert_selected():
            selection = keywords_listbox.curselection()
            if selection:
                keyword = keywords_listbox.get(selection[0])
                self.insert_keyword_link(keyword)
                dialog.destroy()

        def cancel_dialog():
            dialog.destroy()

        ttk.Button(button_frame, text="Insert", command=insert_selected).pack(side=tk.RIGHT, padx=(5, 0))
        ttk.Button(button_frame, text="Cancel", command=cancel_dialog).pack(side=tk.RIGHT)

        # Bind events
        def on_search_change(*args):
            search_term = search_var.get().lower()
            keywords_listbox.delete(0, tk.END)

            filtered_keywords = [k for k in available_keywords if search_term in k.lower()]
            for keyword in filtered_keywords:
                keywords_listbox.insert(tk.END, keyword)

            # Update count label
            if search_term:
                count_label.config(text=f"{len(filtered_keywords)} matches")
            else:
                count_label.config(text=f"{len(filtered_keywords)} keywords")

            if filtered_keywords:
                keywords_listbox.selection_set(0)

        def on_list_double_click(event):
            insert_selected()

        def on_enter_key(event):
            insert_selected()

        search_var.trace("w", on_search_change)
        keywords_listbox.bind("<Double-1>", on_list_double_click)
        keywords_listbox.bind("<Return>", on_enter_key)
        search_entry.bind("<Return>", on_enter_key)

        # Initialize count label
        count_label.config(text=f"{len(available_keywords)} keywords")

        # Focus on search entry
        search_entry.focus()
        if available_keywords:
            keywords_listbox.selection_set(0)

        # Wait for dialog to close
        dialog.wait_window()

    def insert_keyword_link(self, keyword):
        """Insert keyword link at current cursor position"""
        # Get current cursor position
        cursor_pos = self.content_text.index(tk.INSERT)

        # Create the markdown link
        link_text = f"[{keyword}]({keyword.lower()}.md)"

        # Insert the link at cursor position
        self.content_text.insert(cursor_pos, link_text)

        # Update the data
        content = self.content_text.get(1.0, tk.END).rstrip()
        if self.current_keyword_key in self.keywords_data:
            self.keywords_data[self.current_keyword_key]['content'] = content

        # Update status
        self.status_var.set(f"Inserted link to {keyword}")

    def create_status_bar(self):
        """Create the status bar"""
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(self.main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))

    def load_file(self, file_path):
        """Load keywords from JSON file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                self.keywords_data = json.load(f)

            self.file_path = file_path
            self.keyword_keys = list(self.keywords_data.keys())
            self.update_keywords_list()
            self.status_var.set(f"Loaded {len(self.keyword_keys)} keywords from {os.path.basename(file_path)}")
            self.root.title(f"NextBuild Keywords Editor - {os.path.basename(file_path)}")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {str(e)}")

    def save_file(self):
        """Save keywords to JSON file"""
        if not self.file_path:
            return self.save_file_as()

        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(self.keywords_data, f, indent=2, ensure_ascii=False)

            self.status_var.set(f"Saved {len(self.keyword_keys)} keywords to {os.path.basename(self.file_path)}")
            return True

        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {str(e)}")
            return False

    def save_file_as(self):
        """Save keywords to a new file"""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )

        if file_path:
            self.file_path = file_path
            return self.save_file()

        return False

    def open_file(self):
        """Open a keywords file"""
        file_path = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )

        if file_path:
            self.load_file(file_path)

    def update_keywords_list(self):
        """Update the keywords listbox"""
        self.keywords_listbox.delete(0, tk.END)

        # Filter keywords based on search and category
        search_term = self.search_var.get().lower()
        category_filter = self.category_filter.get()

        filtered_keys = []
        for key in self.keyword_keys:
            if key in self.keywords_data:
                keyword_data = self.keywords_data[key]

                # Search filter
                if search_term and search_term not in key.lower():
                    continue

                # Category filter
                if category_filter != "All":
                    if keyword_data.get('category', '') != category_filter:
                        continue

                filtered_keys.append(key)

        # Update listbox
        for key in filtered_keys:
            self.keywords_listbox.insert(tk.END, key)

        # Update status
        if search_term or category_filter != "All":
            self.status_var.set(f"Showing {len(filtered_keys)} of {len(self.keyword_keys)} keywords")
        else:
            self.status_var.set(f"Total: {len(self.keyword_keys)} keywords")

    def on_keyword_select(self, event):
        """Handle keyword selection"""
        selection = self.keywords_listbox.curselection()
        if selection:
            index = selection[0]
            keyword_key = self.keywords_listbox.get(index)

            if keyword_key in self.keywords_data:
                self.current_keyword_key = keyword_key
                self.load_keyword_to_editor(keyword_key)

    def new_keyword(self):
        """Create a new keyword"""
        # Find a unique name
        base_name = "NEW_KEYWORD"
        counter = 1
        keyword_name = base_name

        while keyword_name in self.keywords_data:
            keyword_name = f"{base_name}_{counter}"
            counter += 1

        # Create new keyword data
        new_data = {
            "content": f"# {keyword_name}\n\n## Description\n\nDescription here...\n",
            "category": "keywords",
            "showInKeywordList": False,
            "isManualOnly": False
        }

        self.keywords_data[keyword_name] = new_data
        self.keyword_keys.append(keyword_name)
        self.update_keywords_list()

        # Select the new keyword
        try:
            index = self.keyword_keys.index(keyword_name)
            filtered_index = self.get_filtered_index(keyword_name)
            if filtered_index >= 0:
                self.keywords_listbox.selection_set(filtered_index)
                self.keywords_listbox.see(filtered_index)
                self.load_keyword_to_editor(keyword_name)
        except ValueError:
            pass

        self.status_var.set(f"Created new keyword: {keyword_name}")

    def delete_keyword(self):
        """Delete the current keyword"""
        if not self.current_keyword_key:
            messagebox.showwarning("Warning", "No keyword selected")
            return

        if messagebox.askyesno("Confirm Delete",
                             f"Are you sure you want to delete keyword '{self.current_keyword_key}'?"):
            del self.keywords_data[self.current_keyword_key]
            self.keyword_keys.remove(self.current_keyword_key)

            self.update_keywords_list()
            self.clear_editor()
            self.current_keyword_key = None
            self.status_var.set(f"Deleted keyword: {self.current_keyword_key}")

    def duplicate_keyword(self):
        """Duplicate the current keyword"""
        if not self.current_keyword_key:
            messagebox.showwarning("Warning", "No keyword selected")
            return

        # Find a unique name
        base_name = f"{self.current_keyword_key}_COPY"
        counter = 1
        new_name = base_name

        while new_name in self.keywords_data:
            new_name = f"{base_name}_{counter}"
            counter += 1

        # Duplicate the data
        self.keywords_data[new_name] = self.keywords_data[self.current_keyword_key].copy()
        self.keyword_keys.append(new_name)
        self.update_keywords_list()

        # Select the new keyword
        try:
            filtered_index = self.get_filtered_index(new_name)
            if filtered_index >= 0:
                self.keywords_listbox.selection_set(filtered_index)
                self.keywords_listbox.see(filtered_index)
                self.load_keyword_to_editor(new_name)
        except ValueError:
            pass

        self.status_var.set(f"Duplicated keyword: {new_name}")

    def clear_editor(self):
        """Clear the editor fields"""
        self.keyword_entry.delete(0, tk.END)
        self.category_entry.set('')
        self.show_in_list_var.set(False)
        self.manual_only_var.set(False)
        self.content_text.delete(1.0, tk.END)

    def get_filtered_index(self, keyword_name):
        """Get the index of a keyword in the filtered listbox"""
        for i in range(self.keywords_listbox.size()):
            if self.keywords_listbox.get(i) == keyword_name:
                return i
        return -1

    def on_keyword_name_change(self, event=None):
        """Handle keyword name changes"""
        if not self.current_keyword_key:
            return

        new_name = self.keyword_entry.get().strip()
        if not new_name or new_name == self.current_keyword_key:
            return

        # Check if name already exists
        if new_name in self.keywords_data and new_name != self.current_keyword_key:
            messagebox.showwarning("Warning", f"Keyword '{new_name}' already exists")
            self.keyword_entry.delete(0, tk.END)
            self.keyword_entry.insert(0, self.current_keyword_key)
            return

        # Rename the keyword
        self.keywords_data[new_name] = self.keywords_data.pop(self.current_keyword_key)
        index = self.keyword_keys.index(self.current_keyword_key)
        self.keyword_keys[index] = new_name
        self.current_keyword_key = new_name

        self.update_keywords_list()

        # Update selection
        filtered_index = self.get_filtered_index(new_name)
        if filtered_index >= 0:
            self.keywords_listbox.selection_set(filtered_index)

    def on_category_change(self, event=None):
        """Handle category changes"""
        if not self.current_keyword_key:
            return

        new_category = self.category_entry.get()
        if self.current_keyword_key in self.keywords_data:
            self.keywords_data[self.current_keyword_key]['category'] = new_category

    def on_show_in_list_change(self):
        """Handle show in list checkbox changes"""
        if not self.current_keyword_key:
            return

        if self.current_keyword_key in self.keywords_data:
            self.keywords_data[self.current_keyword_key]['showInKeywordList'] = self.show_in_list_var.get()

    def on_manual_only_change(self):
        """Handle manual only checkbox changes"""
        if not self.current_keyword_key:
            return

        if self.current_keyword_key in self.keywords_data:
            self.keywords_data[self.current_keyword_key]['isManualOnly'] = self.manual_only_var.get()

    def on_content_change(self, event=None):
        """Handle content changes"""
        if not self.current_keyword_key:
            return

        content = self.content_text.get(1.0, tk.END).rstrip()
        if self.current_keyword_key in self.keywords_data:
            self.keywords_data[self.current_keyword_key]['content'] = content

    def on_search_change(self, event=None):
        """Handle search input changes"""
        self.update_keywords_list()

    def on_filter_change(self, event=None):
        """Handle category filter changes"""
        self.update_keywords_list()

    def sort_by_name(self):
        """Sort keywords by name"""
        self.keyword_keys.sort()
        self.update_keywords_list()

    def sort_by_category(self):
        """Sort keywords by category"""
        self.keyword_keys.sort(key=lambda x: self.keywords_data[x].get('category', ''))
        self.update_keywords_list()

    def clean_content(self):
        """Clean content by removing problematic characters and formatting"""
        if not self.current_keyword_key:
            messagebox.showwarning("Warning", "No keyword selected")
            return

        content = self.content_text.get(1.0, tk.END)

        # Clean common issues
        original_content = content

        # Remove trailing whitespace from each line
        lines = content.split('\n')
        cleaned_lines = []
        for line in lines:
            # Remove trailing whitespace but preserve single trailing newline
            cleaned_line = line.rstrip()
            cleaned_lines.append(cleaned_line)

        # Rejoin lines, preserving final newline if it existed
        content = '\n'.join(cleaned_lines)
        if original_content.endswith('\n'):
            content += '\n'

        # Remove any non-printable characters (except newlines and tabs)
        content = re.sub(r'[^\x20-\x7E\n\t]', '', content)

        # Remove multiple consecutive empty lines (more than 2)
        content = re.sub(r'\n{3,}', '\n\n', content)

        # Update the text widget
        self.content_text.delete(1.0, tk.END)
        self.content_text.insert(1.0, content)

        # Update the data
        if self.current_keyword_key in self.keywords_data:
            self.keywords_data[self.current_keyword_key]['content'] = content

        # Show cleanup summary
        removed_chars = len(original_content) - len(content)
        self.status_var.set(f"Cleaned content: removed {removed_chars} problematic characters")

    def format_markdown(self):
        """Apply basic markdown formatting improvements"""
        if not self.current_keyword_key:
            messagebox.showwarning("Warning", "No keyword selected")
            return

        content = self.content_text.get(1.0, tk.END)
        original_content = content

        # Basic markdown formatting improvements
        lines = content.split('\n')
        formatted_lines = []

        for i, line in enumerate(lines):
            # Ensure proper header formatting
            if line.strip().startswith('#'):
                # Add blank line before headers (except first line)
                if i > 0 and formatted_lines and formatted_lines[-1].strip():
                    formatted_lines.append('')

                # Ensure proper spacing after #
                line = re.sub(r'^#+\s*', lambda m: m.group().replace(' ', ''), line)
                line = re.sub(r'^#+', lambda m: m.group() + ' ', line)

            # Ensure blank lines around code blocks
            elif line.strip().startswith('```'):
                if i > 0 and formatted_lines and formatted_lines[-1].strip():
                    formatted_lines.append('')
                formatted_lines.append(line)
                if i < len(lines) - 1 and lines[i + 1].strip():
                    formatted_lines.append('')
                continue

            # Ensure proper list formatting
            elif re.match(r'^\s*[\-\*\+]\s', line):
                line = re.sub(r'^(\s*)[\-\*\+]\s*', r'\1- ', line)

            # Ensure proper numbered list formatting
            elif re.match(r'^\s*\d+\.\s', line):
                line = re.sub(r'^(\s*)\d+\.\s*', lambda m: f"{m.group(1)}1. ", line)

            formatted_lines.append(line)

        content = '\n'.join(formatted_lines)

        # Update the text widget
        self.content_text.delete(1.0, tk.END)
        self.content_text.insert(1.0, content)

        # Update the data
        if self.current_keyword_key in self.keywords_data:
            self.keywords_data[self.current_keyword_key]['content'] = content

        self.status_var.set("Applied markdown formatting improvements")

    def update_preview(self):
        """Update the markdown preview"""
        if not self.current_keyword_key:
            return

        content = self.content_text.get(1.0, tk.END)

        # Convert markdown to HTML with extensions
        # Note: tkhtmlview doesn't support <style> tags, only inline styles
        html_content = markdown.markdown(
            content,
            extensions=['fenced_code', 'tables', 'sane_lists']
        )

        # tkhtmlview doesn't support CSS in <style> tags
        # It only supports basic HTML with default styling
        # Just pass the converted markdown HTML directly
        self.preview_text.set_html(html_content)

    def on_content_change(self, event=None):
        """Handle content changes"""
        if not self.current_keyword_key:
            return

        content = self.content_text.get(1.0, tk.END).rstrip()
        if self.current_keyword_key in self.keywords_data:
            self.keywords_data[self.current_keyword_key]['content'] = content

        # Don't auto-update preview - it causes performance issues
        # User can click "Refresh Preview" button instead

    def load_keyword_to_editor(self, keyword_key):
        """Load keyword data into the editor"""
        if keyword_key not in self.keywords_data:
            return

        data = self.keywords_data[keyword_key]

        # Update fields
        self.keyword_entry.delete(0, tk.END)
        self.keyword_entry.insert(0, keyword_key)

        self.category_entry.set(data.get('category', ''))

        self.show_in_list_var.set(data.get('showInKeywordList', False))
        self.manual_only_var.set(data.get('isManualOnly', False))

        # Update content
        self.content_text.delete(1.0, tk.END)
        self.content_text.insert(1.0, data.get('content', ''))

        # Preview is not auto-updated for performance reasons
        # User can click "Refresh Preview" button when needed

    def show_about(self):
        """Show about dialog"""
        messagebox.showinfo("About",
                          "NextBuild Keywords Editor\n\n"
                          "A GUI application for editing NextBuild keywords JSON files.\n\n"
                          "Features:\n"
                          "• Add, edit, delete, and duplicate keywords\n"
                          "• Search and filter functionality\n"
                          "• Live editing with automatic saving\n"
                          "• Tabbed content editor (Edit/Preview modes)\n"
                          "• Markdown preview and formatting tools\n"
                          "• Content cleaning (removes trailing whitespace)\n"
                          "• Right-click context menu for keyword linking\n"
                          "• Searchable keyword dialog (handles 400+ keywords)\n"
                          "• Keyboard shortcut Ctrl+K for quick linking\n"
                          "• Support for all keyword properties\n"
                          "• Companion cleaning script for batch processing")


def main():
    root = tk.Tk()
    app = KeywordsEditor(root)
    root.mainloop()


if __name__ == "__main__":
    main()
