import sqlite3

def CreateDatabase():
    #We use ':memory:' to create a database in RAM!
    connection = sqlite3.connect(':memory:')
    with connection:
        cur = connection.cursor()
        #We begin by actually making the table
        cur.execute("CREATE TABLE if not exists Roster( \
            Name TEXT, \
            Species TEXT, \
            IQ INT \
            );")

        #We now create a tuple of the values we want to enter...
        ourValues = (("Jean-Baptiste Zorg", "Human", 122), ("Korben Dallas", "Meat Popsicle", 100), ("Ak'not", "Mangalore", -5))
        #And enter them all at once thanks to executemany!
        cur.executemany(""" INSERT INTO Roster (Name, Species, IQ) VALUES (?, ?, ?)""", ourValues)

        #Now, we need to change an entry. Specifically, Korben Dallas needs to be marked as Human
        cur.execute("""UPDATE Roster SET Species = 'Human' WHERE Name='Korben Dallas'""")

        #Finally, we select all info for the Humans!
        cur.execute("""SELECT Name, IQ FROM Roster WHERE Species='Human'""")

        #We set a variable to grab the selected data
        varTest2 = cur.fetchall()

        #Then we execute a simple loop to display our results!
        for i in varTest2:
            print("{} is a Human with an IQ of {}".format(i[0], i[1]))
        #I was making this part more complicated than it needed to be... I was trying to use fetchone() here.
        #But, since i in varTest2 is each tuple, using i[0] and i[1] is enough.

    connection.close()

	


if __name__ == "__main__":
    print("Here we go!")
    CreateDatabase()

