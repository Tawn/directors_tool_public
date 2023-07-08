import tkinter as tk
from tkinter import ttk
from data.database import SQLiteDB

class Event(tk.Frame):
    
    def __init__(self, master):
        super().__init__(master)
        self.db = SQLiteDB()
        self.set_layout() # Layout
        self.set_contents() # Contents 
        self.get_events()
        self.summary_output = ""
        self.output_events()

    
    def get_events(self):
        events_list = self.db.get_events()
        self.events = [0]*2400
        for time, event in events_list:
            self.events[time] = event
        
    def set_layout(self):
        # Rows
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1) 

        # Columns
        self.grid_columnconfigure(0, weight=1) 

    def set_contents(self):
        """ Row 0
            - Display Events Section
        """
        self.display_section = tk.LabelFrame(self, text="Events Output")
        self.display_section.grid_rowconfigure(0, weight=1) # Display
        self.display_section.grid_columnconfigure(0, weight=1) # Display Label
        self.display_section.grid(row=0, column=0, sticky="nsew")
        # -- Row 0: Events Output -- #
        self.event_text = tk.Text(self.display_section, wrap="word")
        self.event_text.grid(row=0, column=0, sticky="ew")
        
        """ Row 1
            - Modify Events Section
        """
        self.modify_section = tk.LabelFrame(self, text="Modify Events")
        self.modify_section.grid_rowconfigure(0, weight=1) # Labels
        self.modify_section.grid_rowconfigure(1, weight=1) # Entries

        self.modify_section.grid_columnconfigure(0, weight=1) # Time Label
        self.modify_section.grid_columnconfigure(1, weight=1) # Time Entry
        self.modify_section.grid_columnconfigure(2, weight=1) # Add Button
        self.modify_section.grid_columnconfigure(3, weight=1) # Del Button
        self.modify_section.grid(row=1, column=0, sticky="nsew")
        # -- Row 2: Event Time, Entry, Add, Del -- #
        self.time_label = tk.Label(self.modify_section, text="Time (hhmm)")        
        self.time_entry = tk.Entry(self.modify_section)
        self.add_button = tk.Button(self.modify_section, text="Add", command=lambda: self.add_event())
        self.delete_button = tk.Button(self.modify_section, text="Del", command=lambda: self.delete_event())
        # Layout
        self.time_label.grid(row=0, column=0, sticky="e")
        self.time_entry.grid(row=0, column=1, sticky="w")
        self.add_button.grid(row=0, column=2 ,sticky="ew")       
        self.delete_button.grid(row=0, column=3, sticky="ew")
        
        # -- Row 3: Event entry
        self.desc_text = tk.Text(self.modify_section, wrap="word")
        self.desc_text.grid(row=1, column=0, sticky="ew", columnspan=4)
        

        
    def add_event(self):
        self.event_text.delete("1.0", tk.END)
        try:
            time = int(self.time_entry.get())
            if time < 0 or time >= 2400:
                self.event_text.insert(tk.END, "Invalid number format")
            else: 
                desc = self.desc_text.get("1.0", "end-1c")
                # Delete if Empty
                if desc == '':
                    self.db.delete_event(time)
                # Add New Event
                elif self.events[time] == 0: 
                    self.db.add_event(time, desc)
                # Update Event
                else: 
                    self.db.update_event(time, desc)
                self.output_events()
        except ValueError:
            self.event_text.insert(tk.END, "Invalid number format")
    
    def delete_event(self):
        try:
            time = int(self.time_entry.get())
            self.db.delete_event(time)
            self.output_events()
        except ValueError:
            self.event_text.insert(tk.END, "Invalid number format")
            
    def output_events(self):
        self.get_events()
        self.event_text.configure(state=tk.NORMAL)
        self.event_text.delete("1.0", tk.END)
        self.output = ""
        self.summary_output = ""
        for i in range(0, 2400):
            if self.events[i] != 0:
                if self.events[i] == "":
                    self.events[i] = 0
                elif i == 0:
                    self.output += "0000: " + self.events[i] + "\n\n"
                    self.summary_output += "\t0000: " + self.events[i] + "\n\n"
                elif i < 10:
                    self.output += "000" + str(i) + ": " + self.events[i] + "\n\n"
                    self.summary_output += "\t000" + str(i) + ": " + self.events[i] + "\n\n"
                elif i < 100:
                    self.output += "00" + str(i) + ": " + self.events[i] + "\n\n"
                    self.summary_output += "\t00" + str(i) + ": " + self.events[i] + "\n\n"
                elif i < 1000:
                    self.output += "0" + str(i) + ": " + self.events[i] + "\n\n"
                    self.summary_output += "\t0" + str(i) + ": " + self.events[i] + "\n\n"
                else:
                    self.output += str(i) + ": " + self.events[i] + "\n\n"
                    self.summary_output += "\t" + str(i) + ": " + self.events[i] + "\n\n"
        self.event_text.insert(tk.END, self.output)
        self.event_text.configure(state=tk.DISABLED)
