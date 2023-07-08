import tkinter as tk
from tkinter import ttk
from data.database import SQLiteDB
class Agenda(tk.Frame):
    
    def __init__(self, master):
        super().__init__(master)
        self.db = SQLiteDB() # Database
        self.set_layout() # Layout
        self.set_contents() # Contents
        self.display_agenda()
        self.agenda_output = ""
        self.summary_output = "" 
        self.directors_output = "" 
        self.set_agenda_output()
        self.set_summary_output()
        self.set_directors_output()
        
    def set_layout(self):
        # Rows
        self.grid_rowconfigure(0, weight=1) # Modify Agenda Section
        self.grid_rowconfigure(1, weight=1) # Labels
        self.grid_rowconfigure(2, weight=1) # Output
        self.grid_rowconfigure(3, weight=1) # Summary Section

        # Columns
        self.grid_columnconfigure(0, weight=1) # Cat1
        self.grid_columnconfigure(1, weight=1) # Cat2
        self.grid_columnconfigure(2, weight=1) # Cat3
        
    def set_contents(self):
        """ Row 0
            - Modify Agenda Section
        """
        self.modify_section = tk.LabelFrame(self, text="Modify Agenda")
        self.modify_section.grid_rowconfigure(0, weight=1) # Labels
        self.modify_section.grid_rowconfigure(1, weight=1) # Entries
        self.modify_section.grid_rowconfigure(2, weight=1) # Buttons

        self.modify_section.grid_columnconfigure(0, weight=1) # Category
        self.modify_section.grid_columnconfigure(1, weight=1) # Task 
        self.modify_section.grid_columnconfigure(2, weight=1) # Status
        self.modify_section.grid(row=0, column=0, sticky="new", columnspan=3)
        
        entry_label_row = 0
        # Category Label
        self.category_label = tk.Label(self.modify_section, text="Category")
        self.category_label.grid(row=entry_label_row, column=0, sticky="ew")
        # CAT2 Label
        self.task_label = tk.Label(self.modify_section, text="Task")
        self.task_label.grid(row=entry_label_row, column=1, sticky="ew")
        # Status Label
        self.status_entry_label = tk.Label(self.modify_section, text="Status")
        self.status_entry_label.grid(row=entry_label_row, column=2, sticky="ew")

        entry_row = 1
        # Location Selection Box
        self.selected_value = tk.StringVar()
        self.category_combobox = ttk.Combobox(self.modify_section, textvariable=self.selected_value)
        options = ["CAT1", "CAT2", "CAT3"]
        self.category_combobox['values'] = options
        self.category_combobox.current(0)
        self.category_combobox.grid(row=entry_row, column=0, sticky="ew")
        # Name Entry
        self.task_entry = tk.Entry(self.modify_section)
        self.task_entry.grid(row=entry_row, column=1, sticky="ew") 
        # Status Selection Box
        self.selected_value2 = tk.StringVar()
        self.status_combobox = ttk.Combobox(self.modify_section, textvariable=self.selected_value2)
        options = ["Incomplete", "Complete"]
        self.status_combobox['values'] = options
        self.status_combobox.current(0)
        self.status_combobox.grid(row=entry_row, column=2, sticky="ew") 

        button_row = 2
        # Add Button
        self.add_button = tk.Button(self.modify_section, text="ADD", command=lambda: self.add_task())
        self.add_button.grid(row=button_row, column=0, sticky="ew")  
        # Set Button
        self.set_button = tk.Button(self.modify_section, text="UPDATE", command=lambda: self.update_task())
        self.set_button.grid(row=button_row, column=1, sticky="ew")  
        # Del Button
        self.del_button = tk.Button(self.modify_section, text="DELETE", command=lambda: self.delete_task())
        self.del_button.grid(row=button_row, column=2, sticky="ew") 
    
        """ Row 1
            - Locations Labels
        """
        locations_row = 1
        # YRP Label
        self.cat1_label = tk.Label(self, text="CAT1")
        # Not at YRP Label
        self.cat2_label = tk.Label(self, text="CAT2")
        # Area Label
        self.cat3_label = tk.Label(self, text="CAT3")
        # Layout
        self.cat1_label.grid(row=locations_row, column=0, sticky="sew")
        self.cat2_label.grid(row=locations_row, column=1, sticky="sew")
        self.cat3_label.grid(row=locations_row, column=2, sticky="sew")

        """ Row 2
            - Listboxes
        """
        output_row = 2
        
        # YRP Listbox
        self.cat1_listbox = tk.Listbox(self)
        self.cat1_listbox.bind("<<ListboxSelect>>", self.cat1_listbox_select)
        # Not at YRP Listbox
        self.cat2_listbox = tk.Listbox(self)
        self.cat2_listbox.bind("<<ListboxSelect>>", self.cat2_listbox_select)
        # Area Listbox
        self.cat3_listbox = tk.Listbox(self)
        self.cat3_listbox.bind("<<ListboxSelect>>", self.cat3_listbox_select)
        # Layout
        self.cat1_listbox.grid(row=output_row, column=0, sticky="nsew", columnspan=1)      
        self.cat2_listbox.grid(row=output_row, column=1, sticky="nsew", columnspan=1)      
        self.cat3_listbox.grid(row=output_row, column=2, sticky="nsew", columnspan=1)  
        
        """ Row 3
            - Summary Section
        """
        summary_section_row = 3
        # Summary Label
        self.summary_section = tk.LabelFrame(self, text="Summary")
        self.summary_section.grid_rowconfigure(0, weight=1)
        self.summary_section.grid_columnconfigure(0, weight=1)
        self.summary_section.grid(row=summary_section_row, column=0, sticky="ew", columnspan=3)
        
        """ Row 6
            - Text Box Entry
        """
        # Summary Text Box
        self.summary_text = tk.Text(self.summary_section, wrap="word")
        self.summary_text.grid(row=0, column=0, sticky="ew")

    def display_agenda(self):
        # Clear Listbox
        self.cat1_listbox.delete(0, tk.END)
        self.cat2_listbox.delete(0, tk.END)
        self.cat3_listbox.delete(0, tk.END)
        self.output = ""
        
        # Retreive Agenda
        self.agenda = self.db.get_agenda()
                
        # Allocate Listboxes
        for i in range (0, len(self.agenda)):
            category = self.agenda[i][0]
            task = self.agenda[i][1]
            status = self.agenda[i][3]
            if category == 'CAT1': 
                self.cat1_listbox.insert(tk.END, task)
                if status == 1:
                    self.cat1_listbox.itemconfig(self.cat1_listbox.size()-1, fg='green')
                else: 
                    self.cat1_listbox.itemconfig(self.cat1_listbox.size()-1, fg='')
            elif category == 'CAT2':
                self.cat2_listbox.insert(tk.END, task)
                if status == 1:
                    self.cat2_listbox.itemconfig(self.cat2_listbox.size()-1, fg='green')
                else: 
                    self.cat2_listbox.itemconfig(self.cat2_listbox.size()-1, fg='')
            else:
                self.cat3_listbox.insert(tk.END, task) 
                if status == 1:
                    self.cat3_listbox.itemconfig(self.cat3_listbox.size()-1, fg='green')
                else: 
                    self.cat3_listbox.itemconfig(self.cat3_listbox.size()-1, fg='')                
        
    def add_task(self):
        task = self.task_entry.get()
        category = self.category_combobox.get()
        summary = self.summary_text.get("1.0", "end-1c")
        if task:
            self.db.add_agenda(category, task, summary)
            self.display_agenda()
        else:
            print("no name")
    
    ''' Update Task 
        - Update task's Cat and Desc
    '''        
    def update_task(self):
        task = self.task_entry.get()
        category = self.category_combobox.get()
        summary = self.summary_text.get("1.0", "end-1c")
        status = 0 if self.status_combobox.get() == 'Incomplete' else 1
        if task:
            self.db.update_agenda(category, task, summary, status)
            self.display_agenda()
        else:
            print("no name")
      
    ''' Delete Task
        - Update task's Cat and Desc
    '''        
    def delete_task(self):
        task = self.task_entry.get()
        if task:
            self.db.delete_agenda(task)
            self.display_agenda()
        else:
            print("no name")    
                    
    ''' Selectable Item Actions '''
    def cat1_listbox_select(self, event):
        if self.cat1_listbox.curselection():
            name = self.cat1_listbox.get(self.cat1_listbox.curselection())
            self.display_info(name)


    def cat2_listbox_select(self, event):
        if self.cat2_listbox.curselection():
            name = self.cat2_listbox.get(self.cat2_listbox.curselection())
            self.display_info(name)

    
    def cat3_listbox_select(self, event):
        if self.cat3_listbox.curselection():
            name = self.cat3_listbox.get(self.cat3_listbox.curselection())
            self.display_info(name)
            
    def display_info(self, name):
        # Clear Entry
        self.task_entry.delete(0, tk.END)
        self.summary_text.delete("1.0", tk.END)

        # Display Category
        task = self.db.get_task_info(name)[0]
        category = task[0]
        if category == 'CAT1':
            self.category_combobox.current(0)
        elif category == 'CAT2':
            self.category_combobox.current(1)
        else: 
            self.category_combobox.current(2)
        
        # Display Task
        self.task_entry.insert(0, name)

        # Display Status
        status = task[3]
        if status == 0:
            self.status_combobox.current(0)
        else: 
            self.status_combobox.current(1)
            
        # Display Summary
        summary = task[2]
        self.summary_text.insert(tk.END, summary)

    ''' Agenda Ouput
        - Goals for today
    '''   
    def set_agenda_output(self):
        cat1 = self.db.get_cat1_agenda()
        cat2 = self.db.get_cat2_agenda()
        cat3 = self.db.get_cat3_agenda()

        # CAT1
        self.agenda_output = "\tCAT1"
        for cat, task, summary, status in cat1:
            self.agenda_output += "\n\t\t" + task
        if len(cat1) == 0:
            self.agenda_output += "\n\t\tTBD"
        
        # CAT2
        self.agenda_output += "\n\tCAT2"
        for cat, task, summary, status in cat2:
            self.agenda_output += "\n\t\t" + task
        if len(cat2) == 0:
            self.agenda_output += "\n\t\tTBD"
          
        # CAT3
        self.agenda_output += "\n\tCAT3"
        for cat, task, summary, status in cat3:
            self.agenda_output += "\n\t\t" + task
        if len(cat3) == 0:
            self.agenda_output += "\n\t\tTBD"
        
    ''' Summary Ouput
        - What's been completed only (No Summary)
    '''   
    def set_summary_output(self):
        cat1 = self.db.get_cat1_agenda()
        cat2 = self.db.get_cat2_agenda()
        cat3 = self.db.get_cat3_agenda()
        count = 0
        # CAT1
        self.summary_output = "\tCAT1"
        for cat, task, summary, status in cat1:
            if status == 1:
                count += 1
                self.summary_output += "\n\t\t" + task 
        if count == 0:
            self.summary_output += "\n\t\tNone"
        
        count = 0
        
        # CAT2
        self.summary_output += "\n\tCAT2"
        for cat, task, summary, status in cat2:
            if status == 1:
                count += 1
                self.summary_output += "\n\t\t" + task 
        if count == 0:
            self.summary_output += "\n\t\tNone"
          
        count = 0
        
        # CAT3
        self.summary_output += "\n\tCAT3"
        for cat, task, summary, status in cat3:
            if status == 1:
                count += 1
                self.summary_output += "\n\t\t" + task 
        if count == 0:
            self.summary_output += "\n\t\tNone"
    
    ''' Director's Ouput
        - What's been completed w/Summary
    '''
    def set_directors_output(self):
        cat1 = self.db.get_cat1_agenda()
        cat2 = self.db.get_cat2_agenda()
        cat3 = self.db.get_cat3_agenda()
        count = 0
        # CAT1
        self.directors_output = "\tCAT1"
        for cat, task, summary, status in cat1:
            if status == 1:
                count += 1
                self.directors_output += "\n\t\t" + task 
                if summary != "Not yet set" and summary != '':
                    self.directors_output += "\n\t\t\t" + summary 
                else: 
                    self.directors_output += "\n\t\t\tNo summary yet"
        if count == 0:
            self.directors_output += "\n\t\tNone"
        
        count = 0
        
        # CAT2
        self.directors_output += "\n\tCAT2"
        for cat, task, summary, status in cat2:
            if status == 1:
                count += 1
                self.directors_output += "\n\t\t" + task 
                if summary != "Not yet set" and summary != '':
                    self.directors_output += "\n\t\t\t" + summary 
                else: 
                    self.directors_output += "\n\t\t\tNo summary yet"
        if count == 0:
            self.directors_output += "\n\t\tNone"
          
        count = 0
        
        # CAT3
        self.directors_output += "\n\tCAT3"
        for cat, task, summary, status in cat3:
            if status == 1:
                count += 1
                self.directors_output += "\n\t\t" + task 
                if summary != "Not yet set" and summary != '':
                    self.directors_output += "\n\t\t\t" + summary 
                else: 
                    self.directors_output += "\n\t\t\tNo summary yet"
        if count == 0:
            self.directors_output += "\n\t\tNone"
            