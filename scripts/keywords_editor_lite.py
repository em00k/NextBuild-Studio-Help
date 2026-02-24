#!/usr/bin/env python3
"""
NextBuild Keywords Editor (Lite)
Zero external dependencies - just Python 3 + tkinter

Usage:
    python keywords_editor_lite.py [filename.json]
"""

import json
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import sys
from pathlib import Path


class KeywordsEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("NextBuild Keywords Editor")
        self.root.geometry("1200x800")

        self.data = {}
        self.current_key = None
        self.file_path = None
        self.modified = False

        # Variables
        self.search_var = tk.StringVar()
        self.search_var.trace('w', lambda *_: self.refresh_list())
        self.category_var = tk.StringVar(value="All")
        self.status_var = tk.StringVar(value="Ready")

        self._build_ui()
        self._bind_keys()
        self._auto_load()

    def _build_ui(self):
        # Main paned window - resizable split
        paned = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # LEFT: List panel
        left = ttk.Frame(paned)
        paned.add(left, weight=1)

        # Search bar
        search_frame = ttk.Frame(left)
        search_frame.pack(fill=tk.X, pady=(0, 5))
        ttk.Label(search_frame, text="Search:").pack(side=tk.LEFT)
        ttk.Entry(search_frame, textvariable=self.search_var).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # Category filter
        self.category_combo = ttk.Combobox(search_frame, textvariable=self.category_var,
                                           values=["All"], state="readonly", width=12)
        self.category_combo.pack(side=tk.LEFT)
        self.category_combo.bind('<<ComboboxSelected>>', lambda _: self.refresh_list())

        # Keywords listbox with scrollbar
        list_frame = ttk.Frame(left)
        list_frame.pack(fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set,
                                   font=("Consolas", 10), exportselection=False)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.listbox.yview)
        self.listbox.bind('<<ListboxSelect>>', self._on_select)

        # Count label
        self.count_label = ttk.Label(left, text="0 keywords")
        self.count_label.pack(anchor=tk.W)

        # RIGHT: Editor panel
        right = ttk.Frame(paned)
        paned.add(right, weight=2)

        # Keyword name (editable)
        name_frame = ttk.Frame(right)
        name_frame.pack(fill=tk.X, pady=(0, 5))
        ttk.Label(name_frame, text="Keyword:", width=10).pack(side=tk.LEFT)
        self.name_entry = ttk.Entry(name_frame, font=("Consolas", 11, "bold"))
        self.name_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.name_entry.bind('<FocusOut>', self._on_name_change)
        self.name_entry.bind('<Return>', self._on_name_change)

        # Category
        cat_frame = ttk.Frame(right)
        cat_frame.pack(fill=tk.X, pady=(0, 5))
        ttk.Label(cat_frame, text="Category:", width=10).pack(side=tk.LEFT)
        self.cat_entry = ttk.Combobox(cat_frame, values=["keywords", "manual", "esxdos", "nextlib", "constants"])
        self.cat_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.cat_entry.bind('<<ComboboxSelected>>', self._on_field_change)
        self.cat_entry.bind('<FocusOut>', self._on_field_change)

        # Checkboxes
        check_frame = ttk.Frame(right)
        check_frame.pack(fill=tk.X, pady=(0, 10))
        self.show_var = tk.BooleanVar()
        self.manual_var = tk.BooleanVar()
        self.hover_var = tk.BooleanVar()
        ttk.Checkbutton(check_frame, text="Show in Keyword List",
                        variable=self.show_var, command=self._on_field_change).pack(side=tk.LEFT, padx=(0, 20))
        ttk.Checkbutton(check_frame, text="Manual Only",
                        variable=self.manual_var, command=self._on_field_change).pack(side=tk.LEFT, padx=(0, 20))
        ttk.Checkbutton(check_frame, text="Show in Hover Help",
                        variable=self.hover_var, command=self._on_field_change).pack(side=tk.LEFT)

        # Toolbar
        toolbar = ttk.Frame(right)
        toolbar.pack(fill=tk.X, pady=(0, 5))
        ttk.Button(toolbar, text="New", command=self.new_keyword, width=8).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="Delete", command=self.delete_keyword, width=8).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="Duplicate", command=self.duplicate_keyword, width=8).pack(side=tk.LEFT, padx=2)
        ttk.Separator(toolbar, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=10)
        ttk.Button(toolbar, text="Insert Link", command=self.insert_link, width=10).pack(side=tk.LEFT, padx=2)

        # Content notebook (Edit / Preview tabs)
        self.notebook = ttk.Notebook(right)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Edit tab
        edit_frame = ttk.Frame(self.notebook)
        self.notebook.add(edit_frame, text="Edit")

        self.content_text = tk.Text(edit_frame, wrap=tk.WORD, font=("Consolas", 10), undo=True)
        content_scroll = ttk.Scrollbar(edit_frame, command=self.content_text.yview)
        self.content_text.config(yscrollcommand=content_scroll.set)
        content_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.content_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.content_text.bind('<KeyRelease>', self._on_content_change)

        # Preview tab
        preview_frame = ttk.Frame(self.notebook)
        self.notebook.add(preview_frame, text="Preview")

        self.preview_text = tk.Text(preview_frame, wrap=tk.WORD, font=("Consolas", 10), state=tk.DISABLED)
        preview_scroll = ttk.Scrollbar(preview_frame, command=self.preview_text.yview)
        self.preview_text.config(yscrollcommand=preview_scroll.set)
        preview_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.preview_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Configure preview tags for basic markdown highlighting
        self.preview_text.tag_configure("h1", font=("Consolas", 14, "bold"), foreground="#0066cc")
        self.preview_text.tag_configure("h2", font=("Consolas", 12, "bold"), foreground="#0066cc")
        self.preview_text.tag_configure("h3", font=("Consolas", 11, "bold"), foreground="#0066cc")
        self.preview_text.tag_configure("code", font=("Consolas", 10), background="#f0f0f0")
        self.preview_text.tag_configure("bold", font=("Consolas", 10, "bold"))
        self.preview_text.tag_configure("link", foreground="#0066cc", underline=True)

        self.notebook.bind('<<NotebookTabChanged>>', self._on_tab_change)

        # Status bar
        status = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN)
        status.pack(fill=tk.X, side=tk.BOTTOM)

        # Menu bar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open...", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As...", command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self._on_close)

        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="New Keyword", command=self.new_keyword, accelerator="Ctrl+N")
        edit_menu.add_command(label="Delete Keyword", command=self.delete_keyword, accelerator="Del")
        edit_menu.add_command(label="Duplicate", command=self.duplicate_keyword, accelerator="Ctrl+D")
        edit_menu.add_separator()
        edit_menu.add_command(label="Insert Link", command=self.insert_link, accelerator="Ctrl+K")

        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="View", menu=view_menu)
        view_menu.add_command(label="Sort A-Z", command=lambda: self.refresh_list(sort='name'))
        view_menu.add_command(label="Sort by Category", command=lambda: self.refresh_list(sort='category'))

    def _bind_keys(self):
        self.root.bind('<Control-s>', lambda _: self.save_file())
        self.root.bind('<Control-o>', lambda _: self.open_file())
        self.root.bind('<Control-n>', lambda _: self.new_keyword())
        self.root.bind('<Control-d>', lambda _: self.duplicate_keyword())
        self.root.bind('<Control-k>', lambda _: self.insert_link())
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    def _auto_load(self):
        """Auto-load from command line arg or default path"""
        if len(sys.argv) > 1:
            self.load_file(sys.argv[1])
        else:
            default = Path(__file__).parent.parent / "jsonfiles" / "keywords.json"
            if default.exists():
                self.load_file(str(default))

    def load_file(self, path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
            self.file_path = path
            self.modified = False
            self._update_categories()
            self.refresh_list()
            self.root.title(f"Keywords Editor - {os.path.basename(path)}")
            self.status_var.set(f"Loaded {len(self.data)} keywords from {os.path.basename(path)}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load: {e}")

    def save_file(self):
        if not self.file_path:
            return self.save_as()
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
            self.modified = False
            self.status_var.set(f"Saved {len(self.data)} keywords")
            return True
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save: {e}")
            return False

    def save_as(self):
        path = filedialog.asksaveasfilename(defaultextension=".json",
                                            filetypes=[("JSON", "*.json"), ("All", "*.*")])
        if path:
            self.file_path = path
            return self.save_file()
        return False

    def open_file(self):
        path = filedialog.askopenfilename(filetypes=[("JSON", "*.json"), ("All", "*.*")])
        if path:
            self.load_file(path)

    def _update_categories(self):
        cats = sorted(set(v.get('category', '') for v in self.data.values() if v.get('category')))
        self.category_combo['values'] = ["All"] + cats

    def refresh_list(self, sort=None):
        """Refresh the keywords listbox"""
        self.listbox.delete(0, tk.END)

        search = self.search_var.get().lower()
        cat_filter = self.category_var.get()

        keys = list(self.data.keys())

        # Always sort alphabetically by default, or by category if requested
        if sort == 'category':
            keys.sort(key=lambda k: (self.data[k].get('category', ''), k.lower()))
        else:
            keys.sort(key=str.lower)

        # Filter
        filtered = []
        for k in keys:
            if search and search not in k.lower():
                continue
            if cat_filter != "All" and self.data[k].get('category') != cat_filter:
                continue
            filtered.append(k)

        for k in filtered:
            self.listbox.insert(tk.END, k)

        self.count_label.config(text=f"{len(filtered)} / {len(self.data)} keywords")

    def _on_select(self, event=None):
        sel = self.listbox.curselection()
        if not sel:
            return
        key = self.listbox.get(sel[0])
        if key not in self.data:
            return

        self.current_key = key
        d = self.data[key]

        # Populate fields
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, key)

        self.cat_entry.set(d.get('category', ''))
        self.show_var.set(d.get('showInKeywordList', False))
        self.manual_var.set(d.get('isManualOnly', False))
        self.hover_var.set(d.get('showInHoverHelp', False))

        self.content_text.delete('1.0', tk.END)
        self.content_text.insert('1.0', d.get('content', ''))

        self.status_var.set(f"Editing: {key}")

    def _on_name_change(self, event=None):
        if not self.current_key:
            return
        new_name = self.name_entry.get().strip()
        if not new_name or new_name == self.current_key:
            return
        if new_name in self.data:
            messagebox.showwarning("Warning", f"'{new_name}' already exists")
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, self.current_key)
            return

        # Rename
        self.data[new_name] = self.data.pop(self.current_key)
        self.current_key = new_name
        self.modified = True
        self.refresh_list()
        self._select_key(new_name)

    def _on_field_change(self, event=None):
        if not self.current_key or self.current_key not in self.data:
            return
        d = self.data[self.current_key]
        d['category'] = self.cat_entry.get()
        d['showInKeywordList'] = self.show_var.get()
        d['isManualOnly'] = self.manual_var.get()
        d['showInHoverHelp'] = self.hover_var.get()
        self.modified = True

    def _on_content_change(self, event=None):
        if not self.current_key or self.current_key not in self.data:
            return
        self.data[self.current_key]['content'] = self.content_text.get('1.0', tk.END).rstrip()
        self.modified = True

    def _on_tab_change(self, event=None):
        """Update preview when switching to preview tab"""
        if self.notebook.index(self.notebook.select()) == 1:  # Preview tab
            self._update_preview()

    def _update_preview(self):
        """Render markdown with basic highlighting"""
        content = self.content_text.get('1.0', tk.END)

        self.preview_text.config(state=tk.NORMAL)
        self.preview_text.delete('1.0', tk.END)

        for line in content.split('\n'):
            if line.startswith('### '):
                self.preview_text.insert(tk.END, line[4:] + '\n', 'h3')
            elif line.startswith('## '):
                self.preview_text.insert(tk.END, line[3:] + '\n', 'h2')
            elif line.startswith('# '):
                self.preview_text.insert(tk.END, line[2:] + '\n', 'h1')
            elif line.startswith('```'):
                self.preview_text.insert(tk.END, line + '\n', 'code')
            else:
                self.preview_text.insert(tk.END, line + '\n')

        self.preview_text.config(state=tk.DISABLED)

    def _select_key(self, key):
        """Select a key in the listbox"""
        for i in range(self.listbox.size()):
            if self.listbox.get(i) == key:
                self.listbox.selection_clear(0, tk.END)
                self.listbox.selection_set(i)
                self.listbox.see(i)
                break

    def new_keyword(self):
        name = "NEW_KEYWORD"
        i = 1
        while name in self.data:
            name = f"NEW_KEYWORD_{i}"
            i += 1

        self.data[name] = {
            "content": f"# {name}\n\nDescription here...\n",
            "category": "keywords",
            "showInKeywordList": False,
            "isManualOnly": False,
            "showInHoverHelp": False
        }
        self.modified = True
        self.refresh_list()
        self._select_key(name)
        self._on_select()
        self.name_entry.focus()
        self.name_entry.select_range(0, tk.END)

    def delete_keyword(self):
        if not self.current_key:
            return
        if messagebox.askyesno("Confirm", f"Delete '{self.current_key}'?"):
            del self.data[self.current_key]
            self.current_key = None
            self.modified = True
            self.refresh_list()
            self._clear_editor()

    def duplicate_keyword(self):
        if not self.current_key:
            return
        new_name = f"{self.current_key}_COPY"
        i = 1
        while new_name in self.data:
            new_name = f"{self.current_key}_COPY_{i}"
            i += 1

        self.data[new_name] = self.data[self.current_key].copy()
        self.modified = True
        self.refresh_list()
        self._select_key(new_name)
        self._on_select()

    def insert_link(self):
        """Show dialog to insert a keyword link"""
        if not self.current_key:
            return

        dialog = tk.Toplevel(self.root)
        dialog.title("Insert Keyword Link")
        dialog.geometry("350x450")
        dialog.transient(self.root)
        dialog.grab_set()

        # Search
        ttk.Label(dialog, text="Search:").pack(anchor=tk.W, padx=10, pady=(10, 0))
        search_var = tk.StringVar()
        search_entry = ttk.Entry(dialog, textvariable=search_var)
        search_entry.pack(fill=tk.X, padx=10, pady=5)

        # List
        frame = ttk.Frame(dialog)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        scroll = ttk.Scrollbar(frame)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        listbox = tk.Listbox(frame, yscrollcommand=scroll.set, font=("Consolas", 10))
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll.config(command=listbox.yview)

        all_keys = sorted([k for k in self.data.keys() if k != self.current_key], key=str.lower)

        def update_list(*_):
            listbox.delete(0, tk.END)
            s = search_var.get().lower()
            for k in all_keys:
                if not s or s in k.lower():
                    listbox.insert(tk.END, k)
            if listbox.size() > 0:
                listbox.selection_set(0)

        def insert():
            sel = listbox.curselection()
            if sel:
                kw = listbox.get(sel[0])
                link = f"[{kw}]({kw}.md)"
                self.content_text.insert(tk.INSERT, link)
                self._on_content_change()
            dialog.destroy()

        search_var.trace('w', update_list)
        update_list()

        # Buttons
        btn_frame = ttk.Frame(dialog)
        btn_frame.pack(fill=tk.X, padx=10, pady=10)
        ttk.Button(btn_frame, text="Insert", command=insert).pack(side=tk.RIGHT, padx=5)
        ttk.Button(btn_frame, text="Cancel", command=dialog.destroy).pack(side=tk.RIGHT)

        listbox.bind('<Double-1>', lambda _: insert())
        listbox.bind('<Return>', lambda _: insert())
        search_entry.bind('<Return>', lambda _: insert())
        search_entry.focus()

    def _clear_editor(self):
        self.name_entry.delete(0, tk.END)
        self.cat_entry.set('')
        self.show_var.set(False)
        self.manual_var.set(False)
        self.hover_var.set(False)
        self.content_text.delete('1.0', tk.END)

    def _on_close(self):
        if self.modified:
            r = messagebox.askyesnocancel("Unsaved Changes", "Save before closing?")
            if r is None:
                return
            if r:
                if not self.save_file():
                    return
        self.root.destroy()


def main():
    root = tk.Tk()
    KeywordsEditor(root)
    root.mainloop()


if __name__ == "__main__":
    main()
