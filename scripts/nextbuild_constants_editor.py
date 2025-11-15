#!/usr/bin/env python3
"""
NextBuild Constants Editor GUI
A Python GUI application for editing NextBuild constants JSON files

Usage:
    python nextbuild_constants_editor.py [filename.json]

If no filename is provided, attempts to auto-load ../data/nextbuild_constants.json
"""

import json
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os
import sys
from pathlib import Path


class ConstantsEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("NextBuild Constants Editor")
        self.root.geometry("1000x700")

        # Initialize variables
        self.constants_data = {}
        self.current_constant_key = None
        self.constant_keys = []
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

        # Create left panel (constants list)
        self.create_constants_list()

        # Create right panel (editor)
        self.create_editor_panel()

        # Create status bar
        self.create_status_bar()

        # Bind keyboard shortcuts
        self.root.bind('<Control-s>', lambda e: self.save_file())
        self.root.bind('<Control-o>', lambda e: self.open_file())
        self.root.bind('<Control-n>', lambda e: self.new_constant())
        self.root.bind('<Delete>', lambda e: self.delete_constant_and_refocus())
        self.root.bind('<KP_Delete>', lambda e: self.delete_constant_and_refocus())  # Numeric keypad delete

        # Auto-load constants file from command line or default location
        file_to_load = None

        # Check for command line argument
        if len(sys.argv) > 1:
            file_to_load = sys.argv[1]
        else:
            # Fall back to default location
            default_path = Path("../data/nextbuild_constants.json").resolve()
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
        edit_menu.add_command(label="New Constant", command=self.new_constant, accelerator="Ctrl+N")
        edit_menu.add_command(label="Delete Constant", command=self.delete_constant)
        edit_menu.add_separator()
        edit_menu.add_command(label="Duplicate Constant", command=self.duplicate_constant)

        # View menu
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="View", menu=view_menu)
        view_menu.add_command(label="Sort by Name", command=self.sort_by_name)
        view_menu.add_command(label="Sort by Value", command=self.sort_by_value)

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

        # Constant operations
        ttk.Button(toolbar, text="New", command=self.new_constant).grid(row=0, column=3, padx=2)
        ttk.Button(toolbar, text="Delete", command=self.delete_constant).grid(row=0, column=4, padx=2)
        ttk.Button(toolbar, text="Duplicate", command=self.duplicate_constant).grid(row=0, column=5, padx=2)

        ttk.Separator(toolbar, orient=tk.VERTICAL).grid(row=0, column=6, sticky=(tk.N, tk.S), padx=5)

        # Navigation
        ttk.Button(toolbar, text="◀ Prev", command=self.prev_constant).grid(row=0, column=7, padx=2)
        ttk.Button(toolbar, text="Next ▶", command=self.next_constant).grid(row=0, column=8, padx=2)

        ttk.Separator(toolbar, orient=tk.VERTICAL).grid(row=0, column=9, sticky=(tk.N, tk.S), padx=5)

        # Sort options
        ttk.Button(toolbar, text="Sort A-Z", command=self.sort_by_name).grid(row=0, column=10, padx=2)
        ttk.Button(toolbar, text="Sort by Value", command=self.sort_by_value).grid(row=0, column=11, padx=2)

    def create_constants_list(self):
        """Create the constants list panel"""
        # Left panel frame
        left_frame = ttk.LabelFrame(self.main_frame, text="Constants", padding="5")
        left_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 5))

        # Search frame
        search_frame = ttk.Frame(left_frame)
        search_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 5))

        ttk.Label(search_frame, text="Search:").grid(row=0, column=0, sticky=tk.W)
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        self.search_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(5, 0))
        self.search_entry.bind('<KeyRelease>', self.filter_constants)

        search_frame.columnconfigure(1, weight=1)

        # Constants list
        list_frame = ttk.Frame(left_frame)
        list_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Create Treeview for constants
        self.constants_tree = ttk.Treeview(list_frame, columns=("value", "type"), show="tree headings", height=20)
        self.constants_tree.heading("#0", text="Constant Name")
        self.constants_tree.heading("value", text="Value")
        self.constants_tree.heading("type", text="Type")
        self.constants_tree.column("#0", width=200)
        self.constants_tree.column("value", width=100)
        self.constants_tree.column("type", width=80)

        # Scrollbars for tree
        tree_scroll_y = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.constants_tree.yview)
        tree_scroll_x = ttk.Scrollbar(list_frame, orient=tk.HORIZONTAL, command=self.constants_tree.xview)
        self.constants_tree.configure(yscrollcommand=tree_scroll_y.set, xscrollcommand=tree_scroll_x.set)

        self.constants_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        tree_scroll_y.grid(row=0, column=1, sticky=(tk.N, tk.S))
        tree_scroll_x.grid(row=1, column=0, sticky=(tk.W, tk.E))

        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)

        # Bind selection event
        self.constants_tree.bind('<<TreeviewSelect>>', self.on_constant_select)

        left_frame.columnconfigure(0, weight=1)
        left_frame.rowconfigure(1, weight=1)

    def create_editor_panel(self):
        """Create the editor panel"""
        # Right panel frame
        right_frame = ttk.LabelFrame(self.main_frame, text="Editor", padding="5")
        right_frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Constant info frame
        info_frame = ttk.Frame(right_frame)
        info_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))

        ttk.Label(info_frame, text="Constant Name:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.name_var = tk.StringVar()
        self.name_entry = ttk.Entry(info_frame, textvariable=self.name_var, width=50)
        self.name_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(5, 0), pady=2)
        self.name_entry.bind('<KeyRelease>', self.on_name_change)

        # Value type selection
        ttk.Label(info_frame, text="Value Type:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.value_type_var = tk.StringVar(value="number")
        self.value_type_combo = ttk.Combobox(info_frame, textvariable=self.value_type_var,
                                           values=["number", "string", "boolean", "array"], state="readonly", width=15)
        self.value_type_combo.grid(row=1, column=1, sticky=tk.W, padx=(5, 0), pady=2)
        self.value_type_combo.bind('<<ComboboxSelected>>', self.on_value_type_change)

        info_frame.columnconfigure(1, weight=1)

        # Value editor
        value_frame = ttk.LabelFrame(right_frame, text="Value", padding="5")
        value_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))

        # Simple value entry (for numbers, strings, booleans)
        self.simple_value_var = tk.StringVar()
        self.simple_value_entry = ttk.Entry(value_frame, textvariable=self.simple_value_var)
        self.simple_value_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 5))

        # Array value editor (multi-line)
        self.array_value_text = scrolledtext.ScrolledText(value_frame, height=8)
        # Initially hidden - will be shown when array type is selected

        # Bind change events
        self.simple_value_entry.bind('<KeyRelease>', self.on_field_change)

        # Description editor
        desc_frame = ttk.LabelFrame(right_frame, text="Description", padding="5")
        desc_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.desc_text = scrolledtext.ScrolledText(desc_frame, height=6)
        self.desc_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Bind change event
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
            title="Open Constants File",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            initialdir="../data"
        )
        if file_path:
            self.load_file(file_path)

    def load_file(self, file_path):
        """Load constants from JSON file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                self.constants_data = json.load(f)

            self.file_path = file_path
            self.constant_keys = list(self.constants_data.keys())
            self.current_index = 0
            self.current_constant_key = self.constant_keys[0] if self.constant_keys else None

            self.update_constants_list()
            if self.current_constant_key:
                self.display_constant(self.current_constant_key)

            self.status_var.set(f"Loaded {len(self.constant_keys)} constants from {os.path.basename(file_path)}")
            self.root.title(f"NextBuild Constants Editor - {os.path.basename(file_path)}")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {str(e)}")

    def save_file(self):
        """Save constants to JSON file"""
        if not self.file_path:
            return self.save_file_as()

        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(self.constants_data, f, indent=2, ensure_ascii=False)

            self.status_var.set(f"Saved {len(self.constant_keys)} constants to {os.path.basename(self.file_path)}")
            messagebox.showinfo("Success", "File saved successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {str(e)}")

    def save_file_as(self):
        """Save constants to a new JSON file"""
        file_path = filedialog.asksaveasfilename(
            title="Save Constants File As",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            initialdir="../data",
            defaultextension=".json"
        )
        if file_path:
            self.file_path = file_path
            self.save_file()

    def update_constants_list(self):
        """Update the constants list in the treeview"""
        # Clear existing items
        for item in self.constants_tree.get_children():
            self.constants_tree.delete(item)

        # Filter constants based on search
        search_term = self.search_var.get().lower()
        filtered_keys = [key for key in self.constant_keys if search_term in key.lower()]

        # Add filtered constants to tree
        for key in filtered_keys:
            constant = self.constants_data[key]
            value = constant.get('value', '')
            value_type = self.get_value_type(value)
            display_value = self.format_value_for_display(value)

            self.constants_tree.insert('', tk.END, text=key, values=(display_value, value_type))

    def get_value_type(self, value):
        """Get the type of a value"""
        if isinstance(value, bool):
            return "boolean"
        elif isinstance(value, (int, float)):
            return "number"
        elif isinstance(value, str):
            return "string"
        elif isinstance(value, list):
            return "array"
        else:
            return "unknown"

    def parse_number_value(self, value_str):
        """Parse a number value, supporting hex with $ prefix and binary with % prefix"""
        value_str = value_str.strip()
        if value_str.startswith('$'):
            # Hex value with $ prefix
            try:
                return int(value_str[1:], 16)
            except ValueError:
                return 0
        elif value_str.startswith('%'):
            # Binary value with % prefix
            try:
                return int(value_str[1:], 2)
            except ValueError:
                return 0
        else:
            # Regular decimal or float
            try:
                if '.' in value_str:
                    return float(value_str)
                else:
                    return int(value_str)
            except ValueError:
                return 0

    def format_number_for_display(self, value):
        """Format a number for display in decimal format"""
        if isinstance(value, float):
            return str(value)
        elif isinstance(value, int):
            return str(value)
        else:
            return str(value)

    def format_value_for_display(self, value):
        """Format value for display in the tree"""
        if isinstance(value, list):
            return f"[{len(value)} items]"
        elif isinstance(value, str) and len(value) > 20:
            return f'"{value[:20]}..."'
        else:
            return str(value)

    def filter_constants(self, event=None):
        """Filter constants based on search term"""
        self.update_constants_list()

    def on_constant_select(self, event):
        """Handle constant selection in the treeview"""
        selection = self.constants_tree.selection()
        if selection:
            item = selection[0]
            constant_name = self.constants_tree.item(item, 'text')
            if constant_name in self.constants_data:
                self.current_constant_key = constant_name
                self.current_index = self.constant_keys.index(constant_name)
                self.display_constant(constant_name)

    def display_constant(self, constant_key):
        """Display a constant in the editor"""
        if constant_key not in self.constants_data:
            return

        constant = self.constants_data[constant_key]

        # Update fields
        self.name_var.set(constant_key)

        # Update value and type
        value = constant.get('value', '')
        value_type = self.get_value_type(value)
        self.value_type_var.set(value_type)

        self.update_value_editor(value, value_type)

        # Update description
        self.desc_text.delete(1.0, tk.END)
        self.desc_text.insert(1.0, constant.get('description', ''))

        self.status_var.set(f"Editing: {constant_key}")

    def update_value_editor(self, value, value_type):
        """Update the value editor based on type"""
        if value_type == "array":
            # Show array editor, hide simple editor
            self.simple_value_entry.grid_remove()
            self.array_value_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

            # Populate array text
            if isinstance(value, list):
                self.array_value_text.delete(1.0, tk.END)
                for item in value:
                    self.array_value_text.insert(tk.END, f"{item}\n")
            else:
                self.array_value_text.delete(1.0, tk.END)

            # Bind array change event
            self.array_value_text.bind('<KeyRelease>', self.on_field_change)

        else:
            # Show simple editor, hide array editor
            self.array_value_text.grid_remove()
            self.simple_value_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 5))

            # Populate simple value
            if value_type == "string":
                self.simple_value_var.set(f'"{value}"' if isinstance(value, str) else str(value))
            elif value_type == "number":
                self.simple_value_var.set(self.format_number_for_display(value))
            else:
                self.simple_value_var.set(str(value))

            # Bind simple change event
            self.simple_value_entry.bind('<KeyRelease>', self.on_field_change)

    def on_name_change(self, event=None):
        """Handle constant name change"""
        new_name = self.name_var.get().strip()
        if new_name and new_name != self.current_constant_key:
            # Check if name already exists
            if new_name in self.constants_data and new_name != self.current_constant_key:
                messagebox.showwarning("Warning", "A constant with this name already exists!")
                self.name_var.set(self.current_constant_key)
                return

            # Rename the constant
            if self.current_constant_key in self.constants_data:
                self.constants_data[new_name] = self.constants_data.pop(self.current_constant_key)
                self.constant_keys[self.current_index] = new_name
                self.current_constant_key = new_name
                self.update_constants_list()
                self.status_var.set(f"Renamed to: {new_name}")

    def on_value_type_change(self, event=None):
        """Handle value type change"""
        value_type = self.value_type_var.get()
        current_value = self.constants_data[self.current_constant_key].get('value', '')

        # Convert current value to new type if possible
        if value_type == "array":
            if not isinstance(current_value, list):
                current_value = [current_value] if current_value != '' else []
        elif value_type == "number":
            try:
                if isinstance(current_value, str):
                    if current_value.startswith('"') and current_value.endswith('"'):
                        current_value = current_value[1:-1]
                    current_value = self.parse_number_value(current_value)
                elif isinstance(current_value, (int, float)):
                    current_value = current_value  # Already a number
                else:
                    current_value = 0
            except:
                current_value = 0
        elif value_type == "string":
            if not isinstance(current_value, str):
                current_value = str(current_value)
        elif value_type == "boolean":
            current_value = bool(current_value)

        self.constants_data[self.current_constant_key]['value'] = current_value
        self.update_value_editor(current_value, value_type)
        self.update_constants_list()

    def on_field_change(self, event=None):
        """Handle field changes"""
        if not self.current_constant_key:
            return

        # Update the constant data
        value_type = self.value_type_var.get()

        if value_type == "array":
            # Parse array from text
            array_text = self.array_value_text.get(1.0, tk.END).strip()
            if array_text:
                lines = [line.strip() for line in array_text.split('\n') if line.strip()]
                # Try to convert to appropriate types
                parsed_array = []
                for line in lines:
                    try:
                        # Try to parse as number first
                        if '.' in line:
                            parsed_array.append(float(line))
                        else:
                            parsed_array.append(int(line))
                    except:
                        # If not a number, treat as string
                        parsed_array.append(line)
                self.constants_data[self.current_constant_key]['value'] = parsed_array
            else:
                self.constants_data[self.current_constant_key]['value'] = []
        else:
            # Parse simple value
            simple_value = self.simple_value_var.get().strip()
            if value_type == "number":
                self.constants_data[self.current_constant_key]['value'] = self.parse_number_value(simple_value)
            elif value_type == "string":
                if simple_value.startswith('"') and simple_value.endswith('"'):
                    simple_value = simple_value[1:-1]
                self.constants_data[self.current_constant_key]['value'] = simple_value
            elif value_type == "boolean":
                self.constants_data[self.current_constant_key]['value'] = simple_value.lower() in ('true', '1', 'yes')

        # Update description
        self.constants_data[self.current_constant_key]['description'] = self.desc_text.get(1.0, tk.END).strip()

        # Update the list display
        self.update_constants_list()

    def new_constant(self):
        """Create a new constant"""
        # Find a unique name
        base_name = "NEW_CONSTANT"
        counter = 1
        new_name = base_name
        while new_name in self.constants_data:
            new_name = f"{base_name}_{counter}"
            counter += 1

        # Create new constant
        self.constants_data[new_name] = {
            "value": 0,
            "description": ""
        }

        self.constant_keys.append(new_name)
        self.current_index = len(self.constant_keys) - 1
        self.current_constant_key = new_name

        self.update_constants_list()
        self.display_constant(new_name)

        # Select the new item in the tree
        for item in self.constants_tree.get_children():
            if self.constants_tree.item(item, 'text') == new_name:
                self.constants_tree.selection_set(item)
                self.constants_tree.focus(item)
                break

    def delete_constant(self):
        """Delete the current constant"""
        if not self.current_constant_key:
            return

        if messagebox.askyesno("Confirm Delete", f"Delete constant '{self.current_constant_key}'?"):
            del self.constants_data[self.current_constant_key]
            self.constant_keys.remove(self.current_constant_key)

            if self.constant_keys:
                self.current_index = max(0, self.current_index - 1)
                self.current_constant_key = self.constant_keys[self.current_index]
                self.display_constant(self.current_constant_key)
            else:
                self.current_constant_key = None
                self.clear_editor()

            self.update_constants_list()
            self.status_var.set(f"Deleted: {self.current_constant_key}")

    def delete_constant_and_refocus(self):
        """Delete the current constant and refocus on the list for rapid editing"""
        self.delete_constant()
        # Focus back on the constants list for rapid editing
        self.constants_tree.focus()
        # Select the current item in the tree if there are items left
        if self.constant_keys and self.current_constant_key:
            self.select_current_in_tree()

    def duplicate_constant(self):
        """Duplicate the current constant"""
        if not self.current_constant_key:
            return

        # Find a unique name
        base_name = f"{self.current_constant_key}_COPY"
        counter = 1
        new_name = base_name
        while new_name in self.constants_data:
            new_name = f"{base_name}_{counter}"
            counter += 1

        # Duplicate the constant
        self.constants_data[new_name] = self.constants_data[self.current_constant_key].copy()

        self.constant_keys.append(new_name)
        self.current_index = len(self.constant_keys) - 1
        self.current_constant_key = new_name

        self.update_constants_list()
        self.display_constant(new_name)

    def prev_constant(self):
        """Navigate to previous constant"""
        if self.constant_keys and self.current_index > 0:
            self.current_index -= 1
            self.current_constant_key = self.constant_keys[self.current_index]
            self.display_constant(self.current_constant_key)

            # Update tree selection
            self.select_current_in_tree()

    def next_constant(self):
        """Navigate to next constant"""
        if self.constant_keys and self.current_index < len(self.constant_keys) - 1:
            self.current_index += 1
            self.current_constant_key = self.constant_keys[self.current_index]
            self.display_constant(self.current_constant_key)

            # Update tree selection
            self.select_current_in_tree()

    def select_current_in_tree(self):
        """Select the current constant in the treeview"""
        for item in self.constants_tree.get_children():
            if self.constants_tree.item(item, 'text') == self.current_constant_key:
                self.constants_tree.selection_set(item)
                self.constants_tree.focus(item)
                self.constants_tree.see(item)
                break

    def sort_by_name(self):
        """Sort constants by name"""
        self.constant_keys.sort()
        self.update_constants_list()

    def sort_by_value(self):
        """Sort constants by value (numeric values first, then others)"""
        def sort_key(key):
            value = self.constants_data[key].get('value', '')
            if isinstance(value, (int, float)):
                return (0, value)  # Numbers first
            elif isinstance(value, str):
                return (1, value.lower())  # Strings second
            elif isinstance(value, bool):
                return (2, value)  # Booleans third
            elif isinstance(value, list):
                return (3, len(value))  # Arrays fourth (by length)
            else:
                return (4, str(value))  # Everything else last

        self.constant_keys.sort(key=sort_key)
        self.update_constants_list()

    def clear_editor(self):
        """Clear all editor fields"""
        self.name_var.set("")
        self.simple_value_var.set("")
        self.array_value_text.delete(1.0, tk.END)
        self.desc_text.delete(1.0, tk.END)

    def show_about(self):
        """Show about dialog"""
        messagebox.showinfo("About", "NextBuild Constants Editor\n\nA GUI tool for editing NextBuild JSON constants files.\n\nFeatures:\n• Load and save JSON constants files\n• Edit constant properties\n• Support for multiple value types\n• Navigate between constants\n• Search and filter constants\n• Create, duplicate, and delete constants\n• Sort by name or value")


def main():
    root = tk.Tk()
    app = ConstantsEditor(root)
    root.mainloop()


if __name__ == "__main__":
    main()





