#Here is where we'll keep info related to the GUI for our student register!

from tkinter import *
import tkinter as tk

#Import the other modules created here
import StudentTrackingMain
import StudentTrackingFunctions


def GUI_Layout(self):
    """
    I'm going to use grid geometry to lay out our five fields,
    plus the two buttons for delete and submit!

    Each entry row will have a label, and the entry rows themselves
    should stretch for a few columns.
    """

    
            

    #First Name Label and Positioning
    self.labelFirstName = tk.Label(self.master, text="First Name:")
    self.labelFirstName.grid(row=0, column=0, padx = (10, 0), pady = (20, 0))

    #Last Name Label and Positioning
    self.labelLastName = tk.Label(self.master, text="Last Name:")
    self.labelLastName.grid(row=2, column=0, padx = (10, 0), pady = (20, 0))

    #Phone Number Label and Positioning
    self.labelPhoneNumber = tk.Label(self.master, text="Phone #:")
    self.labelPhoneNumber.grid(row=4, column=0, padx = (10, 0), pady = (20, 0))

    #E-mail Label and Positioning
    self.labelEmail = tk.Label(self.master, text="E-mail:")
    self.labelEmail.grid(row=6, column=0, padx = (10, 0), pady = (20, 0))
    
    #Current Class Label and Positioning
    self.labelCurrentClass = tk.Label(self.master, text="Current Class:")
    self.labelCurrentClass.grid(row=8, column=0, padx = (10, 0), pady = (20, 0))


    #Creating entry boxes now

    #First Name Entry Box
    self.textFirstName = tk.Entry(self.master, text="Testing")
    self.textFirstName.grid(row=1,column=0, columnspan = 2, padx = (10, 0), pady = (10, 0), stick=E+W)

    #Last Name Entry Box
    self.textLastName = tk.Entry(self.master, text="")
    self.textLastName.grid(row=3,column=0, columnspan = 2, padx = (10, 0), pady = (10, 0), stick=E+W)

    #Phone Number Entry Box
    self.textPhoneNumber = tk.Entry(self.master, text="")
    self.textPhoneNumber.grid(row=5,column=0, columnspan = 2, padx = (10, 0), pady = (10, 0), stick=E+W)

    #E-mail Entry Box
    self.textEmail = tk.Entry(self.master, text="")
    self.textEmail.grid(row=7,column=0, columnspan = 2, padx = (10, 0), pady = (10, 0), stick=E+W)

    #Current Class Box
    self.textCurrentClass = tk.Entry(self.master, text="")
    self.textCurrentClass.grid(row=9,column=0, columnspan = 2, padx = (10, 0), pady = (10, 0), stick=E+W)


    #Now for the buttons!

    #Adding the delete button
    self.buttonDeleteButton = tk.Button(self.master, width = 20, height = 2, text = "Delete", command=lambda: StudentTrackingFunctions.deleteEntry(self))
    self.buttonDeleteButton.grid(row=10, column= 0, columnspan = 2, padx = (10, 0), pady = (10, 10))

    #Adding the delete button
    self.buttonSubmitButton = tk.Button(self.master, width = 20, height = 2, text = "Submit", command=lambda: StudentTrackingFunctions.addEntry(self))
    self.buttonSubmitButton.grid(row=10, column=2, columnspan = 2, padx = (10, 0), pady = (10, 10))


    #Now for the dB records so they can be viewed and deleted!

    self.listMainList = Listbox(self.master)
    self.listMainList.bind('<<ListboxSelect>>',lambda event: StudentTrackingFunctions.onSelect(self,event))
    self.listMainList.grid(row = 1, column = 3, rowspan = 9, columnspan = 6, stick=N+E+S+W)


if __name__ == "__main__":
    pass

