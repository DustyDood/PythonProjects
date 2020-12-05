
"""
Hello!

This is my attempt at recreating the Phonebook assignment,
but it is instead for a student tracking database. The functionality
will be a bit more simple, as I only need to add a submit and delete
button that is integrated with the connected database.

The students themselves will have 5 points of info:

1. First Name
2. Last Name
3. Phone Number
4. Email
5. Current Course

Here we go!

POST COMPLETION: I have finished making the GUI!

Honest to goodness... It's not the prettiest. This is meant to be a
rapid exercise, so visuals aren't meant to be as important. Nevertheless,
if I have some spare time (hah!), I should spend it on touching up the GUI.

In terms of functions, this database runs off of just last name instead of full name.
This does cause issues for deleting entries, as last name is not a primary key!
In other words, if you delete an entry with a specific last name, all entries with
that last name are also deleted. The fix to this would be adding a new column to the database
that is a composite key(I hope that's the right one) of the first and last name,
which in turn should be unique... If not, I could go by the autoincrement ID, which
may ultimately be the best idea.
"""


from tkinter import *
import tkinter as tk

#Import the other other modules created here
import StudentTrackingGUI
import StudentTrackingFunctions


# Creating the ParentWindow Class which inherits from Frame!
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master = master

        #Some basic graphical changes, such as the title, bg, and window size
        self.master.title("Student Register")
        self.master.configure(bg = "lightgrey")
        self.master.minsize(800, 500)

        #Calling the GUI_Layout class should position the labels and textboxes
        StudentTrackingGUI.GUI_Layout(self)

        #An attempt at making the grid uniform
        i = 0
        while i < 11:
            print(i)
            root.columnconfigure(i, weight = 1)
            i += 1

        j = 0
        while j < 8:
            print(j)
            root.rowconfigure(j, weight = 1)
            j += 1

        #Spawning the initial database
        StudentTrackingFunctions.CreateDatabase(self)
        #Calling refresh to ensure that all entries are present!
        StudentTrackingFunctions.onRefresh(self)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
