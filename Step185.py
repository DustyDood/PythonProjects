#I'm aiming to go through a list of files, find all that end in .txt,
#and then add all of those into a database!
import sqlite3

#We'll start by establishing the database and connecting to it
conn = sqlite3.connect('step185.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_doclist( \
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    col_fileName TEXT \
    )")
    conn.commit()
conn.close()

#This is the file list provided by Tech Academy.
#We need to go through this list and add in all that end with .txt
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

"""
#I'm making a list and using a for loop to add all files that end with .txt to my list
#Technically, I could write a for loop for the fileList itself.
#I thought it would be better that connecting and closing multiple times.
#But maybe I can? I'll save this code for now.
myList = []
for x in fileList:
    if x.endswith('txt'):
        myList.append(x)
"""


conn = sqlite3.connect('step185.db')

with conn:
    cur = conn.cursor()
    #Like our above list, we're cycling through the list and finding all files that end with .txt
    #If it matchse, it then inserts that value into our table. We only need to enter the file name
    # as the ID is autoincrementing.
    for x in fileList:
        if x.endswith('txt'):
            cur.execute("INSERT INTO tbl_doclist (col_fileName) VALUES (?)", \
                        (x,))

    conn.commit()
conn.close()


        
#Finally,we print out the values stored in the database
conn = sqlite3.connect('step185.db')

with conn:
    cur = conn.cursor()
    #We're grabbing only the file name, as we don't care about the ID that's icrementing
    cur.execute("SELECT col_fileName FROM tbl_doclist")
    storedValues = cur.fetchall()
    #This for loop prints out all the file names as "File Name: X"
    #I'm not sure why the [0] is needed, as there's only one element to the tuple.
    #Maybe it's so that the program knows to grab that specific element in the tuple
    # rather than the whole tuple itself?
    for y in storedValues:
        results = "File Name: {}".format(y[0])
        print(results)
                

                        


