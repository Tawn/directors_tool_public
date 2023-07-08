import tkinter as tk
from tkinter import ttk

from data.database import SQLiteDB

class Team(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.db = SQLiteDB()
        self.set_layout() 
        self.set_contents() 
        self.display_teams()
        self.output = ""
        self.set_output()
        
    def set_output(self):        
        ''' At location1 Output '''
        at_location1 = self.db.get_at_location1()        
        at_location1_output = "At location1: \n\t"        
        if len(at_location1) == 0:
            at_location1_output += "None"
        elif len(at_location1) == 1:
            name = at_location1[0][0]
            desc = at_location1[0][2]
            # No Desc
            if desc == None or desc == 'None':
                at_location1_output += name + "-san."
            # Desc
            else: 
                at_location1_output += name + "-san (" + desc + ")."
        elif len(at_location1) == 2:
            name = at_location1[0][0]
            desc = at_location1[0][2]
            name2 = at_location1[1][0]
            desc2 = at_location1[1][2]
            # No Desc
            if desc == None or desc == 'None':
                at_location1_output += name + "-san and "
            # Desc
            else: 
                at_location1_output += name + "-san (" + desc + ") and "
            # No Desc
            if desc2 == None or desc2 == 'None':
                at_location1_output += name2 + "-san."
            # Desc
            else: 
                at_location1_output += name2 + "-san (" + desc2 + ")."  
        # More than two members
        else:
            for i in range (0, len(at_location1)):
                name = at_location1[i][0]
                desc = at_location1[i][2]
                # not last member
                if i != len(at_location1)-1:
                    # No Desc
                    if desc == None or desc == 'None':
                        at_location1_output += name + "-san, "
                    # Desc
                    else: 
                        at_location1_output += name + "-san (" + desc + "), "
                # Last Member
                else: 
                    # No Desc
                    if desc == None or desc == 'None':
                        at_location1_output += "and " + name + "-san."
                    # Desc
                    else: 
                        at_location1_output += "and " + name + "-san (" + desc + ")."        
       
        ''' Not At location1 Output '''
        not_at_location1 = self.db.get_not_at_location1()        
        not_at_location1_output = "Not at location1: \n\t"  
        if len(not_at_location1) == 0:
            not_at_location1_output += "None"
        elif len(not_at_location1) == 1:
            name = not_at_location1[0][0]
            desc = not_at_location1[0][2]
            # No Desc
            if desc == None or desc == 'None':
                not_at_location1_output += name + "-san."
            # Desc
            else: 
                not_at_location1_output += name + "-san (" + desc + ")."
        elif len(not_at_location1) == 2:
            name = not_at_location1[0][0]
            desc = not_at_location1[0][2]
            name2 = not_at_location1[1][0]
            desc2 = not_at_location1[1][2]
            # No Desc
            if desc == None or desc == 'None':
                not_at_location1_output += name + "-san and "
            # Desc
            else: 
                not_at_location1_output += name + "-san (" + desc + ") and "
            # No Desc
            if desc2 == None or desc2 == 'None':
                not_at_location1_output += name2 + "-san."
            # Desc
            else: 
                not_at_location1_output += name2 + "-san (" + desc2 + ")."  
    
        # More than two members
        else:
            for i in range (0, len(not_at_location1)):
                name = not_at_location1[i][0]
                desc = not_at_location1[i][2]
                # not last member
                if i != len(not_at_location1)-1:
                    # No Desc
                    if desc == None or desc == 'None':
                        not_at_location1_output += name + "-san, "
                    # Desc
                    else: 
                        not_at_location1_output += name + "-san (" + desc + "), "
                # Last Member
                else: 
                    # No Desc
                    if desc == None or desc == 'None':
                        not_at_location1_output += "and " + name + "-san."
                    # Desc
                    else: 
                        not_at_location1_output += "and " + name + "-san (" + desc + ")."
                    
        self.output = at_location1_output + "\n\n" + not_at_location1_output
        
    def set_layout(self):
        # Rows
        self.grid_rowconfigure(0, weight=1) # Modify Members
        self.grid_rowconfigure(1, weight=1) # Move Members
        self.grid_rowconfigure(2, weight=1) # Output Label
        self.grid_rowconfigure(3, weight=10) # Outputs

        # Columns
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1) 
        self.grid_columnconfigure(2, weight=1)

    def set_contents(self):
        # Modify Members
        self.modify_section = tk.LabelFrame(self, text="Modify Members")
        self.modify_section.grid_rowconfigure(0, weight=1)
        self.modify_section.grid_rowconfigure(1, weight=1)
        self.modify_section.grid_rowconfigure(2, weight=1)

        self.modify_section.grid_columnconfigure(0, weight=1)
        self.modify_section.grid_columnconfigure(1, weight=1)
        self.modify_section.grid_columnconfigure(2, weight=1)
        self.modify_section.grid(row=0, column=0, sticky="new", columnspan=3)
        
        """ Row 0
            - Entry Labels
        """
        entry_label_row = 0
        # location1 Label
        self.location_label = tk.Label(self.modify_section, text="Location")
        self.location_label.grid(row=0, column=0, sticky="ew")
        
        # Not at location1 Label
        self.name_label = tk.Label(self.modify_section, text="Name")
        self.name_label.grid(row=0, column=1, sticky="ew")
        
        # Desc Label
        self.location2_entry_label = tk.Label(self.modify_section, text="Description")
        self.location2_entry_label.grid(row=0, column=2, sticky="ew")
        
        entry_row = 1
        # Location Selection Box
        self.selected_value = tk.StringVar()
        self.location_combobox = ttk.Combobox(self.modify_section, textvariable=self.selected_value)
        options = ["location1", "Not at location1", "location2"]
        self.location_combobox['values'] = options
        self.location_combobox.current(0)
        self.location_combobox.grid(row=1, column=0, sticky="ew")
        
        # Name Entry
        self.name_entry = tk.Entry(self.modify_section)
        self.name_entry.grid(row=1, column=1, sticky="ew")
        
        # Description Entry
        self.desc_entry = tk.Entry(self.modify_section)
        self.desc_entry.grid(row=1, column=2, sticky="ew")

        button_row = 2
        # Add Button
        self.add_button = tk.Button(self.modify_section, text="ADD", command=lambda: self.add_member())
        self.add_button.grid(row=button_row, column=0, sticky="ew") 

        # Set Button
        self.set_button = tk.Button(self.modify_section, text="UPDATE", command=lambda: self.update_info())
        self.set_button.grid(row=button_row, column=1, sticky="ew") 
        
        # Del Button
        self.del_button = tk.Button(self.modify_section, text="DELETE", command=lambda: self.delete_member())
        self.del_button.grid(row=button_row, column=2, sticky="ew")  

        """ Row 1
            - Buttons - move
        """
        self.move_member_section = tk.LabelFrame(self, text="Move Members")
        self.move_member_section.grid_rowconfigure(0, weight=1)
        self.move_member_section.grid_columnconfigure(0, weight=1)
        self.move_member_section.grid_columnconfigure(1, weight=1)
        self.move_member_section.grid(row=1, column=0, sticky="sew", columnspan=3)
        
        button_row = 0
        # Left-Move Button
        self.left_move_button = tk.Button(self.move_member_section, text="←", command=lambda: self.move_left())
        self.left_move_button.grid(row=button_row, column=0, sticky="ew")  
        # Right-Move Button
        self.right_move_button = tk.Button(self.move_member_section, text="→", command=lambda: self.move_right())
        self.right_move_button.grid(row=button_row, column=1, sticky="ew")          

        
        """ Row 2
            - Locations Labels
        """
        locations_row = 2
        # location1 Label
        self.location1_label = tk.Label(self, text="location1")
        
        # Not at location1 Label
        self.not_at_location1_label = tk.Label(self, text="Not at location1")
        
        # location2 Label
        self.location2_label = tk.Label(self, text="location2")
        
        # Layout
        self.location1_label.grid(row=locations_row, column=0, sticky="sew", columnspan=1)
        self.not_at_location1_label.grid(row=locations_row, column=1, sticky="sew", columnspan=1)
        self.location2_label.grid(row=locations_row, column=2, sticky="sew", columnspan=1)
        
        """ Row 3
            - Listboxes
        """
        output_row = 3
        
        # location1 Listbox
        self.location1_listbox = tk.Listbox(self)
        self.location1_listbox.bind("<<ListboxSelect>>", self.location1_listbox_select)
        # Not at location1 Listbox
        self.not_at_location1_listbox = tk.Listbox(self)
        self.not_at_location1_listbox.bind("<<ListboxSelect>>", self.not_at_location1_listbox_select)
        # location2 Listbox
        self.location2_listbox = tk.Listbox(self)
        self.location2_listbox.bind("<<ListboxSelect>>", self.location2_listbox_select)
        
        self.location1_listbox.grid(row=output_row, column=0, sticky="nsew", columnspan=1)      
        self.not_at_location1_listbox.grid(row=output_row, column=1, sticky="nsew", columnspan=1)      
        self.location2_listbox.grid(row=output_row, column=2, sticky="nsew", columnspan=1)  

    def move_right(self):
        ''' Move Right
            i. get current location
            ii. 
                - if location1 -> Not at location1
                - if Not at location1 -> location2
            iii. update db
        '''
        name = self.name_entry.get()
        member = self.db.get_member_info(name)
        location = member[0][1]
        desc = member[0][2]
        if location == "location1":
            location = "Not at location1"
        elif location == "Not at location1":
            location = "location2"
        else:
            location = None
        if location: 
            self.db.update_member(name, location, desc)
            self.display_teams()
            
        # Set curselection
        if location: 
            # Get the index where item moved to
            members = self.not_at_location1_listbox.get(0, tk.END) if location == "Not at location1" else self.location2_listbox.get(0, tk.END)
            for i in range (len(members)):
                if members[i] == name: 
                    if location == "Not at location1": 
                        self.not_at_location1_listbox.select_set(i)
                    elif location == "location2":
                        self.location2_listbox.select_set(i)
            


    def move_left(self):
        ''' Move Left
            i. get current location
            ii. 
                - if location2 -> Not at location1
                - if Not at location1 -> location1
            iii. update db
        '''
        name = self.name_entry.get()
        member = self.db.get_member_info(name)
        location = member[0][1]
        desc = member[0][2]
        if location == "location2":
            location = "Not at location1"
        elif location == "Not at location1":
            location = "location1"
        else:
            location = None
        
        if location: 
            self.db.update_member(name, location, desc)
            self.display_teams()
            
        # Set curselection
        if location: 
            # Get the index where item moved to
            members = self.not_at_location1_listbox.get(0, tk.END) if location == "Not at location1" else self.location1_listbox.get(0, tk.END)
            for i in range (len(members)):
                if members[i] == name: 
                    if location == "Not at location1": 
                        self.not_at_location1_listbox.select_set(i)
                    elif location == "location1":
                        self.location1_listbox.select_set(i)

    def add_member(self):
        name = self.name_entry.get()
        location = self.location_combobox.get()
        desc = self.desc_entry.get()
        if name:
            self.db.add_member(name, location, desc)
            self.display_teams()
        else:
            print("no name")
    
    ''' Delete Members
        - Deletes members that matches the Name entry
    '''
    def delete_member(self):
        name = self.name_entry.get()
        if name: 
            self.db.delete_member(name)
            self.display_teams()
        else:
            print("no name")
        
    ''' Update Info
        - Update's member's description
    '''
    def update_info(self): 
        # Extract Info
        name = self.name_entry.get()
        location = self.location_combobox.get()
        desc = self.desc_entry.get() 
        if desc == "" or desc == "None":
            desc = None
        
       
        if name:
            self.db.update_member(name, location, desc)
        else: 
            print("no name")
        self.display_teams()
                
    ''' Teams will all start at location1
        - Name: String
        - Location: "location1"
        - Description: None
    '''
    def display_teams(self):
        # Clear Listbox
        self.location1_listbox.delete(0, tk.END)
        self.not_at_location1_listbox.delete(0, tk.END)
        self.location2_listbox.delete(0, tk.END)
        self.output = ""
        
        # Retreive Members
        self.members = self.db.get_team()
        
        # Allocate Listboxes
        for i in range(0, len(self.members)):
            name = self.members[i][0]
            location = self.members[i][1]
            
            # At location1
            if location == 'location1':
                self.location1_listbox.insert(tk.END, name)

            # Not at location1
            elif location == 'location2':
                self.location2_listbox.insert(tk.END, name)
            
            # location2 Test
            else: 
                self.not_at_location1_listbox.insert(tk.END, name) 
        self.set_output()
            
    def location1_listbox_select(self, event):
        if self.location1_listbox.curselection():
            name = self.location1_listbox.get(self.location1_listbox.curselection())
            self.display_info(name)


    def not_at_location1_listbox_select(self, event):
        if self.not_at_location1_listbox.curselection():
            name = self.not_at_location1_listbox.get(self.not_at_location1_listbox.curselection())
            self.display_info(name)

    
    def location2_listbox_select(self, event):
        if self.location2_listbox.curselection():
            name = self.location2_listbox.get(self.location2_listbox.curselection())
            self.display_info(name)
            
    def display_info(self, name):
         # Clear Entry
        self.name_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        # Display Name
        self.name_entry.insert(0, name)
        # Display Location
        member = self.db.get_member_info(name)[0]
        location = member[1]
        if location == 'location1':
            self.location_combobox.current(0)
        elif location == 'Not at location1':
            self.location_combobox.current(1)
        else: 
            self.location_combobox.current(2)
        # Display Description
        description = member[2]
        self.desc_entry.insert(0, description) if description else self.desc_entry.insert(0, "None")