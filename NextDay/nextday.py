import tkinter as tk
from tkinter import ttk
from data.database import SQLiteDB
class NextDay(tk.Frame):
    
    def __init__(self, master):
        super().__init__(master)
        self.db = SQLiteDB() # Database
        self.set_layout() # Layout
        self.set_contents() # Contents
        self.agenda_output = "" 
        self.set_agenda_output()
        self.display_nextday()
        
    def set_layout(self):
        # Rows
        self.grid_rowconfigure(0, weight=1) # Modify Agenda Section
        self.grid_rowconfigure(1, weight=1) # Labels
        self.grid_rowconfigure(2, weight=10) # Output

        # Columns
        self.grid_columnconfigure(0, weight=1) # CAT1
        self.grid_columnconfigure(1, weight=1) # CAT2
        self.grid_columnconfigure(2, weight=1) # CAT3
        
    def set_contents(self):
        """ Row 0
            - Modify Agenda Section
        """
        self.modify_section = tk.LabelFrame(self, text="Modify Agenda")
        self.modify_section.grid_rowconfigure(0, weight=1) # Labels
        self.modify_section.grid_rowconfigure(1, weight=1) # Entries
        self.modify_section.grid_rowconfigure(2, weight=1) # Buttons

        self.modify_section.grid_columnconfigure(0, weight=1) # Add
        self.modify_section.grid_columnconfigure(1, weight=1) # Update  
        self.modify_section.grid_columnconfigure(2, weight=1) # Delete
        self.modify_section.grid(row=0, column=0, sticky="new", columnspan=3)
        
        entry_label_row = 0
        # Category Label
        self.category_label = tk.Label(self.modify_section, text="Category")
        # CAT2 Label
        self.task_label = tk.Label(self.modify_section, text="Task")
        # Layout
        self.category_label.grid(row=entry_label_row, column=0, sticky="ew")
        self.task_label.grid(row=entry_label_row, column=1, sticky="ew", columnspan=2)
        
        entry_row = 1
        # Location Selection Box
        self.selected_value = tk.StringVar()
        self.category_combobox = ttk.Combobox(self.modify_section, textvariable=self.selected_value)
        options = ["CAT1", "CAT2", "CAT3"]
        self.category_combobox['values'] = options
        self.category_combobox.current(0)
        # Name Entry
        self.task_entry = tk.Entry(self.modify_section)
        # Layout
        self.category_combobox.grid(row=entry_row, column=0, sticky="ew")
        self.task_entry.grid(row=entry_row, column=1, sticky="ew", columnspan=2) 

        button_row = 2
        # Add Button
        self.add_button = tk.Button(self.modify_section, text="ADD", command=lambda: self.add_task())
        # Set Button
        self.set_button = tk.Button(self.modify_section, text="UPDATE", command=lambda: self.update_task())
        # Del Button
        self.del_button = tk.Button(self.modify_section, text="DELETE", command=lambda: self.delete_task())
        # Layout
        self.add_button.grid(row=button_row, column=0, sticky="ew")  
        self.set_button.grid(row=button_row, column=1, sticky="ew")  
        self.del_button.grid(row=button_row, column=2, sticky="ew") 
        
        """ Row 1
            - Category Labels
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
        self.cat1_listbox.grid(row=output_row, column=0, sticky="nsew")      
        self.cat2_listbox.grid(row=output_row, column=1, sticky="nsew")      
        self.cat3_listbox.grid(row=output_row, column=2, sticky="nsew")  

    def display_nextday(self):
        # Clear Listbox
        self.cat1_listbox.delete(0, tk.END)
        self.cat2_listbox.delete(0, tk.END)
        self.cat3_listbox.delete(0, tk.END)
        self.output = ""
        
        # Retreive Agenda
        self.nextday = self.db.get_nextday()
                
        # Allocate Listboxes
        for i in range (0, len(self.nextday)):
            category = self.nextday[i][0]
            task = self.nextday[i][1]
            if category == 'CAT1': 
                self.cat1_listbox.insert(tk.END, task)
            elif category == 'CAT2':
                self.cat2_listbox.insert(tk.END, task)
            else:
                self.cat3_listbox.insert(tk.END, task)                 
        
    def add_task(self):
        task = self.task_entry.get()
        category = self.category_combobox.get()
        if task:
            self.db.add_nextday(category, task)
            self.display_nextday()
        else:
            print("no name")
    
    ''' Update Task 
        - Update task's Cat and Desc
    '''        
    def update_task(self):
        task = self.task_entry.get()
        category = self.category_combobox.get()
        if task:
            self.db.update_nextday(category, task)
            self.display_nextday()
        else:
            print("no name")
      
    ''' Delete Task
        - Update task's Cat and Desc
    '''        
    def delete_task(self):
        task = self.task_entry.get()
        if task:
            self.db.delete_nextday(task)
            self.display_nextday()
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

        # Display Category
        task = self.db.get_nextday_info(name)[0]
        category = task[0]
        if category == 'CAT1':
            self.category_combobox.current(0)
        elif category == 'CAT2':
            self.category_combobox.current(1)
        else: 
            self.category_combobox.current(2)
        
        # Display Task
        self.task_entry.insert(0, name)

   
    ''' Agenda Ouput
        - Goals for today
    '''   
    def set_agenda_output(self):
        cat1 = self.db.get_next_cat1_agenda()
        cat2 = self.db.get_next_cat2_agenda()
        cat3 = self.db.get_next_cat3_agenda()

        # CAT1
        self.agenda_output = "\tCAT1"
        for cat, task in cat1:
            self.agenda_output += "\n\t\t" + task
        if len(cat1) == 0:
            self.agenda_output += "\n\t\tTBD"
        
        # CAT2
        self.agenda_output += "\n\tCAT2"
        for cat, task in cat2:
            self.agenda_output += "\n\t\t" + task
        if len(cat2) == 0:
            self.agenda_output += "\n\t\tTBD"
          
        # CAT3
        self.agenda_output += "\n\tCAT3"
        for cat, task in cat3:
            self.agenda_output += "\n\t\t" + task
        if len(cat3) == 0:
            self.agenda_output += "\n\t\tTBD"