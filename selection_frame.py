import tkinter as tk
from tkinter import ttk
from display_frame import DisplayFrame

class SelectionFrame(tk.Frame):
    def __init__(self, parent, display):
        super().__init__(parent)
        self.set_layout()
        self.set_contents()
        self.display_frame = display
        self.team_button_press()

        
    def set_layout(self):
        # Rows (6)  
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        # # Columns (1)
        self.grid_columnconfigure(0, weight=1)

    def set_contents(self): 
        self.team_button = tk.Button(self, text="Team", command=lambda: self.team_button_press())
        self.agenda_button = tk.Button(self, text="Agenda", command=lambda: self.agenda_button_press())
        self.event_button = tk.Button(self, text="Events", command=lambda: self.event_button_press())
        self.issue_button = tk.Button(self, text="Issues", command=lambda: self.issue_button_press())
        self.next_agenda_button = tk.Button(self, text="Next Test", command=lambda: self.nextday_button_press())
        self.export_button = tk.Button(self, text="Export", command=lambda: self.export_button_press())

        self.team_button.grid(row=0, column=0, sticky="nsew")
        self.agenda_button.grid(row=1, column=0, sticky="nsew")
        self.event_button.grid(row=2, column=0, sticky="nsew")
        self.issue_button.grid(row=3, column=0, sticky="nsew")
        self.next_agenda_button.grid(row=4, column=0, sticky="nsew")
        self.export_button.grid(row=5, column=0, sticky="nsew")
        
    def team_button_press(self):
        self.reset_selection()
        self.team_button.configure(highlightbackground="#3498db")
        self.display_frame.display("team")
    
    def agenda_button_press(self):
        self.reset_selection()
        self.agenda_button.configure(highlightbackground="#3498db")
        self.display_frame.display("agenda")
    
    def event_button_press(self):
        self.reset_selection()
        self.event_button.configure(highlightbackground="#3498db")
        self.display_frame.display("event")
    
    def issue_button_press(self):
        self.reset_selection()
        self.issue_button.configure(highlightbackground="#3498db")
        self.display_frame.display("issue")
    
    def nextday_button_press(self):
        self.reset_selection()
        self.next_agenda_button.configure(highlightbackground="#3498db")
        self.display_frame.display("nextday")
    
    def export_button_press(self):
        self.reset_selection()
        self.export_button.configure(highlightbackground="#3498db")
        self.display_frame.display("export")
        
    
    def reset_selection(self):
        self.team_button.configure(highlightbackground=self.team_button.cget("background"))
        self.agenda_button.configure(highlightbackground=self.agenda_button.cget("background"))
        self.event_button.configure(highlightbackground=self.event_button.cget("background"))
        self.issue_button.configure(highlightbackground=self.issue_button.cget("background"))
        self.next_agenda_button.configure(highlightbackground=self.next_agenda_button.cget("background"))
        self.export_button.configure(highlightbackground=self.export_button.cget("background"))
        
       