import tkinter as tk

root = tk.Tk()

# Create a LabelFrame to group the section with a title
section_frame = tk.LabelFrame(root, text="Section Title", padx=10, pady=10)
section_frame.pack(padx=10, pady=10)

# Add widgets inside the LabelFrame
label1 = tk.Label(section_frame, text="Widget 1")
label1.pack(pady=5)

label2 = tk.Label(section_frame, text="Widget 2")
label2.pack(pady=5)

root.mainloop()
