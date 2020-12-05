"""
My attempt at creating some functions for the Student Tracking Database.
This will be a bit simpler than the phonebook, as we only need two functions:

1. Delete an Entry
2. Submit an Entry

We'll still need to create and connect to the database initially,
but other than that, I imagine things should be pretty straight forward.
"""

from tkinter import *
import tkinter as tk
import sqlite3

#Have to import our other modules
import StudentTrackingMain
import StudentTrackingGUI

def CreateDatabase(self):
    conn = sqlite3.connect('db_studentTracker.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_studentTracker( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_firstName TEXT, \
            col_lastName TEXT, \
            col_phoneNumber TEXT, \
            col_email TEXT, \
            col_currentClass TEXT \
            );")
        conn.commit()
    conn.close()
    initialSetup(self)

def initialSetup(self):
    #This checks to see if we have any values in the dB!
    #If not, it'll enter my info as a default
    conn = sqlite3.connect('db_studentTracker.db')
    with conn:
        cur = conn.cursor()
        cur, count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_studentTracker (col_firstName, col_lastName, col_phoneNumber, col_email, col_currentClass) VALUES (?,?,?,?,?)""", ("Dusty", "Zoland", "555-555-5555", "Justin.d.zoland@gmail.com", "Programming"))
            conn.commit()
    conn.close()

def count_records(cur):
    #This gives us a count of how many entries are in the database
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_studentTracker""")
    count = cur.fetchone()[0]
    return cur,count

def addEntry(self):
    #Grabbing our first and last name entries
    varFirstName = self.textFirstName.get()
    varLastName = self.textLastName.get()
    varPhoneNumber = self.textPhoneNumber.get()
    varEmail = self.textEmail.get()
    varCurrentClass = self.textCurrentClass.get()

    conn = sqlite3.connect('db_studentTracker.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""INSERT INTO tbl_studentTracker (col_firstName, col_lastName, col_phoneNumber, col_email, col_currentClass) VALUES (?,?,?,?,?)""", (varFirstName, varLastName, varPhoneNumber, varEmail, varCurrentClass))
        conn.commit()
    onRefresh(self)
    conn.close()
    
def deleteEntry(self):
    #This will delete an entry selected
    select = self.listMainList.get(self.listMainList.curselection())
    conn = sqlite3.connect('db_studentTracker.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT COUNT(*) FROM tbl_studentTracker""")
        count = cur.fetchone()[0]
        #We're going to allow an entry to be deleted as long as it's not the last one!
        #I won't be implementing all the confirmation messages, as this is a simple version
        if count > 1:
            cur.execute("""DELETE FROM tbl_studentTracker WHERE col_lastName = '{}'""".format(select))
            conn.commit()
            onRefresh(self)
        else:
            print("Can't delete the last entry!")
    conn.close()
                        
            


    

def onRefresh(self):
    self.listMainList.delete(0,END)
    conn = sqlite3.connect('db_studentTracker.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_studentTracker""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
                cursor.execute("""SELECT col_lastname FROM tbl_studentTracker""")
                varList = cursor.fetchall()[i]
                for item in varList:
                    self.listMainList.insert(0,str(item))
                    i = i + 1
    conn.close()


    

def onSelect(self, event):
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('db_studentTracker.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT col_firstName, col_lastName, col_phoneNumber, col_email, col_currentClass FROM tbl_studentTracker WHERE col_lastname = (?)""", [value])
        varBody = cur.fetchall()

        for data in varBody:
            self.textFirstName.delete(0,END)
            self.textFirstName.insert(0,data[0])
            self.textLastName.delete(0,END)
            self.textLastName.insert(0,data[1])
            self.textPhoneNumber.delete(0,END)
            self.textPhoneNumber.insert(0,data[2])
            self.textEmail.delete(0,END)
            self.textEmail.insert(0,data[3])
            self.textCurrentClass.delete(0,END)
            self.textCurrentClass.insert(0,data[4])



if __name__ == "__main__":
    CreateDatabase(self)

