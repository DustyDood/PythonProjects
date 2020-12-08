"""
This file starts by creating a very simple GUI through tkinter.
The user is prompted to enter the heading for their website.
The user types their wanted heading into the entry field, then clicks submit.

By using open(), a basic webpage is created with the user's submission
being a h1 on their website!

"""

import webbrowser
from tkinter import *



def andopen():
    #We start by initializing our GUI
    win = Tk()
    win.title("Make your own web page!")

    #We just want to keep this very simple: We just need
    # a label asking what the user wants their website to display,
    # an entry field where the user can type what they want out,
    # and a submit button to actually generate the website.
    label1 = Label(win, text="What text do you want your website to display?")
    label1.grid(row = 0, column = 1)

    #What the user actually wants is stored as v, which is important
    # for actually passing along the info to the webPageGeneration method!
    v = StringVar()
    entry1 = Entry(win, textvariable = v)
    entry1.grid(row = 1, column = 0, columnspan = 3)

    #I was getting py_var0 initially. I forgot that it was v.get(), not just v!
    submitButton = Button(win, text="Submit", command = lambda: webPageGeneration(v.get()))
    submitButton.grid(row = 2, column = 1)

#This creates our html file using Python!
#Originally, I used x instead of w.
#Since I already created the file with x, I'm just overwriting it now with w.
#The reason why we take a parameter is so that the h1 can generate based
# on the user's entry!
def webPageGeneration(v):
    f = open("VeryBasicWebPage.html", "w")
    f.write("""<html>
                    <body>
                        <h1>
                            {}
                        </h1>
                    </body>
                </html>""".format(v))
    f.close()
    #This will open our html file in a new tab!
    g = webbrowser.open_new_tab("VeryBasicWebPage.html")

if __name__ == "__main__":
    andopen()
