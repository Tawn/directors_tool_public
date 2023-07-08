import tkinter as tk
from tkinter import ttk
from data.database import SQLiteDB

class Issue(tk.Frame):
    
    def __init__(self, master):
        super().__init__(master)
        self.db = SQLiteDB()
        self.set_layout() # Layout
        self.set_contents() # Contents 
        self.output = ""
        self.output_issues()
            
        
    def set_layout(self):
        # Rows
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1) 

        # Columns
        self.grid_columnconfigure(0, weight=1) 

    def set_contents(self):
        """ Row 0
            - Display Issues Section
        """
        self.display_section = tk.LabelFrame(self, text="Issues Output")
        self.display_section.grid_rowconfigure(0, weight=1) # Display
        self.display_section.grid_columnconfigure(0, weight=1) # Display Label
        self.display_section.grid(row=0, column=0, sticky="nsew")
        # -- Row 0: Issues Output -- #
        self.issue_text = tk.Text(self.display_section, wrap="word")
        self.issue_text.grid(row=0, column=0, sticky="ew")
        
        """ Row 1
            - Modify Events Section
        """
        self.modify_section = tk.LabelFrame(self, text="Modify Issues")
        self.modify_section.grid_rowconfigure(0, weight=1) # Labels
        self.modify_section.grid_rowconfigure(1, weight=1) # Entries

        self.modify_section.grid_columnconfigure(0, weight=1) # Time Label
        self.modify_section.grid_columnconfigure(1, weight=1) # Time Entry
        self.modify_section.grid_columnconfigure(2, weight=1) # Add Button
        self.modify_section.grid_columnconfigure(3, weight=1) # Del Button
        self.modify_section.grid(row=1, column=0, sticky="nsew")
        # -- Row 0: Event Time, Entry, Add, Del -- #
        self.number_label = tk.Label(self.modify_section, text="Issue #")
        self.issue_num_entry = tk.Entry(self.modify_section)
        self.add_button = tk.Button(self.modify_section, text="Add", command=lambda: self.add_issue())
        self.delete_button = tk.Button(self.modify_section, text="Del", command=lambda: self.delete_issue())
        # Layout
        self.number_label.grid(row=0, column=0, sticky="e")
        self.issue_num_entry.grid(row=0, column=1, sticky="w")
        self.add_button.grid(row=0, column=2 ,sticky="ew")       
        self.delete_button.grid(row=0, column=3, sticky="ew")
        
        # -- Row 1: Issue entry
        self.desc_text = tk.Text(self.modify_section, wrap="word")
        # Layout
        self.desc_text.grid(row=1, column=0, sticky="ew", columnspan=4)
        
    def add_issue(self):
        try: 
            issue_num  = int(self.issue_num_entry.get())
            desc = self.desc_text.get("1.0", "end-1c")
            self.db.add_issue(issue_num, desc)
            self.output_issues()
        except ValueError: 
            print("invalid input")
    
    def delete_issue(self):
        try: 
            issue_num  = int(self.issue_num_entry.get())
            self.db.delete_issue(issue_num)
            self.output_issues()
        except ValueError: 
            print("invalid input")
    
    def output_issues(self):
        issues = self.db.get_issues()
        self.issue_text.configure(state=tk.NORMAL)
        self.issue_text.delete("1.0", tk.END)
        issues_output = ""
        self.output = ""
        for id, desc in issues:
            issues_output += "Issue #" + str(id) + ":\t" + desc + "\n\n"
            self.output += "\tIssue #" + str(id) + ":\t" + desc + "\n"
        
        if self.output == "":
            self.output = "\tNone\n"
        
        self.issue_text.insert(tk.END, issues_output)
        self.issue_text.configure(state=tk.DISABLED)