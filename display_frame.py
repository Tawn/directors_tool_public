import tkinter as tk
from Team.team import Team
from Agenda.agenda import Agenda
from Event.event import Event
from Issue.issue import Issue
from NextDay.nextday import NextDay
from Export.export import Export

class DisplayFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="red")
        self.set_layout()
        self.display("team")
        
    def set_layout(self):
        # Row
        self.rowconfigure(0, weight=1)
        # Column
        self.grid_columnconfigure(0, weight=1)
        
    def display(self, content):
        if content == "team":
            self.display_frame = Team(self)
        if content == "agenda":
            self.display_frame = Agenda(self)
        if content == "event":
            self.display_frame = Event(self)     
        if content == "issue":
            self.display_frame = Issue(self)  
        if content == "nextday":
            self.display_frame = NextDay(self)  
        if content == "export":
            self.display_frame = Export(self) 
        self.display_frame.forget() 
        self.display_frame.grid(row=0, column=0, sticky="nsew")