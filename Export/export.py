import tkinter as tk
from datetime import datetime

from Team.team import Team
from Agenda.agenda import Agenda
from Issue.issue import Issue
from NextDay.nextday import NextDay
from Event.event import Event

class Export(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.set_layout()
        self.set_contents()
        self.output = ""
        self.cat1_summary = ""
        self.set_cat1_summary()
    
    def set_layout(self):
        # Rows
        self.grid_rowconfigure(0, weight=1) # Start of day Label - Email and Goal's for today
        self.grid_rowconfigure(1, weight=10) # Output Label

        # Columns
        self.grid_columnconfigure(0, weight=1) # Email to CUSTOMER
        self.grid_columnconfigure(1, weight=1) # Today's Summary

    def set_contents(self):
        """ Row 0
            - Buttons
        """
        # Start of Day Label
        self.start_day_section = tk.LabelFrame(self, text="Start of Day")
        self.start_day_section.grid_rowconfigure(0, weight=1)
        self.start_day_section.grid_rowconfigure(1, weight=1)
        self.start_day_section.grid_rowconfigure(2, weight=1)

        self.start_day_section.grid_columnconfigure(0, weight=1)
        self.start_day_section.grid(row=0, column=0, sticky="nsew")
        # Email to CUSTOMER
        self.email_button = tk.Button(self.start_day_section, text="Email Attendance", command=lambda: self.email_button_press())
        self.email_button.grid(row=0, column=0, sticky="ew")         
        # Goal's for today
        self.goals_button = tk.Button(self.start_day_section, text="Goals", command=lambda: self.goals_button_press())
        self.goals_button.grid(row=1, column=0, sticky="ew")  
        
        # End of Day Label
        self.end_day_section = tk.LabelFrame(self, text="End of Day")
        self.end_day_section.grid_rowconfigure(0, weight=1)
        self.end_day_section.grid_rowconfigure(1, weight=1)
        self.end_day_section.grid_rowconfigure(2, weight=1)
        self.end_day_section.grid_columnconfigure(0, weight=1)
        self.end_day_section.grid(row=0, column=1, sticky="nsew")
        # Summary Button - Completed tasks
        self.summary_button = tk.Button(self.end_day_section, text="Today's Summary", command=lambda: self.summary_button_press())
        self.summary_button.grid(row=0, column=0, sticky="ew") 
        # CAT1 Summary Note Button - Plan for next test day
        self.director_button = tk.Button(self.end_day_section, text="CAT1 Test Summary", command=lambda: self.cat1_summary_button_press())
        self.director_button.grid(row=1, column=0, sticky="ew") 
        
        # Director's Summary Note Button - Plan for next test day
        self.director_button = tk.Button(self.end_day_section, text="Director's Notes", command=lambda: self.director_button_press())
        self.director_button.grid(row=2, column=0, sticky="ew") 
        
        """ Row 1
            - Output
        """
        self.display_section = tk.LabelFrame(self, text="Output")
        self.display_section.grid_rowconfigure(0, weight=1) # Display
        self.display_section.grid_columnconfigure(0, weight=1) # Display Label
        self.display_section.grid(row=1, column=0, sticky="nsew", columnspan=2)
        # Output Text
        self.output_text = tk.Text(self.display_section, wrap="word")
        self.output_text.grid(row=0, column=0, sticky="nsew")
    
    # Email Button Press Functions
    def email_button_press(self):   
        # Email Context
        today = datetime.today().strftime("%A, %B %d, %Y")
        email_output = "Good Morning CUSTOMER-san,\n\n" \
                        + "The COMPANY CAT1 Team for today (" + today + ") is as follows:\n\n"
        email_output += Team(self).output
        email_output += "\n\nPlease feel free to contact me with any questions or concerns.\n\n" \
                        + "Best regards,\n"
        
        # Export 
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, email_output)
    
    def goals_button_press(self):
        goals = "Goals for Today:\n" \
                + Agenda(self).agenda_output
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, goals)
    
    def summary_button_press(self):
        agenda_message = "Today's Summary:" \
                            + "\nCompleted:\n" \
                                + Agenda(self).summary_output \
                            + "\nProblems Encountered:\n" \
                                + Issue(self).output \
                            + "\nPlan for next test:\n"\
                                + NextDay(self).agenda_output
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, agenda_message)
    
    def set_cat1_summary(self):
        today = datetime.today().strftime("%Y%m%d")

        self.cat1_summary = "Completed:\n" \
                            + Agenda(self).directors_output \
                        + "\nProblems Encountered:\n" \
                            + Issue(self).output \
                        + "Need Help With\n" \
                            + "\tNone" \
                        + "\nGeneral Notes\n" \
                            + "\tNone" \
                        + "\nPlan for Next Test:\n" \
                            + NextDay(self).agenda_output \
                        + "\nLog Information:\n" \
                            + "ToDo #<#> logs needs to be sent to CUSTOMER." \
                            + "\n\tLogs transferred from SERVER1 to SERVER2: /<PATH>/, /<PATH> to " \
                            + "CUSTOMER for " + today \
                                + "\n\t\SYSTEM1: /<PATH>/" + today \
                                + "\n\t\tSYSTEM2: /<PATH>/" + today
                                
    def cat1_summary_button_press(self):
        today = datetime.today().strftime("%A, %B %d, %Y")
        cat1_summary_output = "Hello all,\n" \
                        + "\nHere is the summary for " + today + " (JST). " \
                        + "If a name is highlight, it means we think you have an action below.\n" \
                        + "\nPlan for today's testing:\n" \
                            + Agenda(self).agenda_output + "\n"
        cat1_summary_output += self.cat1_summary
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, cat1_summary_output)

    def director_button_press(self):
        today = datetime.today().strftime("%A, %B %d, %Y")
        cat1_summary = "Test Director Notes for " + today + " (JST).\n" \
                        + "\nGoals for Today:\n" \
                            + Agenda(self).agenda_output \
                        + "\nTeam Status:\n" \
                            + Team(self).output \
                        + "\nTest Director Log:\n" \
                            + Event(self).summary_output \
                        + "\nToday's Summary:\n" \
                            + self.cat1_summary \
                        + "\nMicrosoft Teams Chat Log:\n" \
                        + "\nSkype Chat Log:\n"
                       
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, cat1_summary)