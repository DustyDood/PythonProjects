#This is a GUI we created earlier in the course, but it will serve its
# purpose quite well for the File Transfer Assignment!

# What we need is a GUI that allows a user to select two folders. The
# first folder is where they want to transfer files from, and the second
# folder is where they want to transfer files to.


from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import FileTransferAssignmentFunc


if __name__ == "__main__":

    #Basic Tk set-up
    win = Tk()
    win.title("File Transfer")

    lbl_overallLabel = Label(win, text="Select where you want to transfer files from and to!")
    lbl_overallLabel.grid(row=0, column=0, columnspan = 4, pady = (10, 0))


    btn_browse1 = Button(win, text="Transfer From:", command = lambda: pathway1())
    btn_browse1.grid(row=1, column = 0, padx = (10, 10), pady=(25, 5), stick = E+W)

    btn_browse2 = Button(win, text="Transfer To:", command = lambda: pathway2())
    btn_browse2.grid(row=2, column = 0, padx = (10, 10), pady=(5, 5), stick = E+W)

    btn_check = Button(win, text="Submit", command = lambda: varCheck())
    btn_check.grid(row = 3, column = 0, padx = (10, 10), pady=(5, 5), stick = E+W)

    btn_close = Button(win, text="Close Program", command = lambda: closeWindow())
    #The padx is so large here to have the entry boxes stretch out across the entire GUI
    #The length is meant to match the picture of a GUI that The Tech Academy had
    btn_close.grid(row = 3, column = 3, padx = (200, 10), pady=(5, 5))

    v1 = StringVar()
    entry_field1 = Entry(win, textvariable = v1)
    entry_field1.grid(row = 1, column = 1, columnspan = 3, padx = (10, 10), pady = (25, 5), stick=E+W)

    v2 = StringVar()
    entry_field2 = Entry(win, textvariable = v2)
    entry_field2.grid(row = 2, column = 1, columnspan = 3, padx = (10, 10), pady = (5, 5), stick = E+W)


def pathway1():
    #Setting our FROM path
    myPath = filedialog.askdirectory()
    v1.set(myPath)

def pathway2():
    #Setting our TO path
    mySecondPath = filedialog.askdirectory()
    v2.set(mySecondPath)
    
def varCheck():
    #We're checking to ensure a FROM and a TO have been set.
    #Otherwise, the file transfer wouldn't work.
    if v1.get() == "" or v2.get() == "":
        messagebox.showinfo("Pathway missing", "You are missing a pathway! Please select a From and a To before continuing")
    #If the pathways have been set, then the transfer function is called!
    #The transfer function returns the number of files that were found to be less than 24 hours old, which is why we store the return in our fileNumber var.
    #For clarity, a message box will tell the user how many files were actually transferred.
    else:
        fileNumber = FileTransferAssignmentFunc.fileTransferGo(v1.get(), v2.get())
        messagebox.showinfo("Transfer complete", "Your transfer is complete! A total of {} files were transferred. Thank you!".format(fileNumber))

#A simple way to close the window
def closeWindow():
    win.destroy()






        
