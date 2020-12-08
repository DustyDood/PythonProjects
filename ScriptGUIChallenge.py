#This is a basic GUI which allows a user to select a file from their directory.
#Then, it stores the pathway for that file

from tkinter import *
from tkinter import filedialog

#Basic Tk set-up
win = Tk()
win.title("Check files")

#Begin by making the required buttons to match the Tech Academy's picture!
btn_browse1 = Button(win, text="Browse...", command = lambda: greetings())
#The pady is higher here to give a little bit of wiggle room at the top
btn_browse1.grid(row=1, column = 0, padx = (10, 10), pady=(25, 5), stick = E+W)
btn_browse2 = Button(win, text="Browse...")
btn_browse2.grid(row=2, column = 0, padx = (10, 10), pady=(5, 5), stick = E+W)
btn_check = Button(win, text="Check for files...")
btn_check.grid(row = 3, column = 0, padx = (10, 10), pady=(5, 5))
btn_close = Button(win, text="Close Program")
#The padx is so large here to have the entry boxes stretch out across the entire GUI
#The length is meant to match the picture of a GUI that The Tech Academy had
btn_close.grid(row = 3, column = 3, padx = (200, 10), pady=(5, 5))

v1 = StringVar()
entry_field1 = Entry(win, textvariable = v1)
entry_field1.grid(row = 1, column = 1, columnspan = 3, padx = (10, 10), pady = (25, 5), stick=E+W)
v2 = StringVar()

entry_field2 = Entry(win, textvariable = v2)
entry_field2.grid(row = 2, column = 1, columnspan = 3, padx = (10, 10), pady = (5, 5), stick = E+W)

def greetings():
    print("Hello!")
    myPath = filedialog.askdirectory()
    v1.set(myPath) 
