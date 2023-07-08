import tkinter as tk

class Popup(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.popup = tk.Toplevel(self)
    
    def show_popup(self):
        self.popup.title("Changes Made")
        self.popup.geometry("200x75")
        self.popup.resizable(False, False)

        label = tk.Label(self.popup, text="Changes have been made!")
        label.pack(pady=20)

        # Close the popup after 3 seconds (3000 milliseconds)
        self.popup.after(3000, self.popup.destroy)
