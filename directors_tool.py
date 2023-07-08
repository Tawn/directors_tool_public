import tkinter as tk
from selection_frame import SelectionFrame
from display_frame import DisplayFrame
from data.database import SQLiteDB

class MainFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.initialize_database()
        self.set_layout()
        self.set_contents()
    
    def initialize_database(self):
        self.db = SQLiteDB()
        self.db.initialize()
        
    def set_layout(self):
        # Row
        self.rowconfigure(0, weight=1)

        # Columns
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=10)
    
    def set_contents(self):
        self.display_frame = DisplayFrame(self)
        self.display_frame.grid(row=0, column=1, sticky="nsew")
        self.selection_frame = SelectionFrame(self, self.display_frame)
        self.selection_frame.grid(row=0, column=0, sticky="nsew")
        
    def set_display(self, content):
        self.display_frame.display(content)
        
if __name__ == "__main__":
    window = tk.Tk()
    window.title("Directors Tool")
    window.geometry("600x400")
    window.minsize(900, 700)
    main_frame = MainFrame(window)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    window.mainloop()
