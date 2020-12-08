import shutil
import os
from datetime import *
import time
import FileTransferAssignmentGUI




def fileTransferGo(p1, p2):

    #set where the files are coming from
    source=(p1 + '/')

    #set where the files are going to
    destination = (p2 + '/')
    files = os.listdir(source)

    #Ok, time for some mathy goodness!
    #currentTime represents the time at the execution
    #of the program, but in seconds.
    currentTime = time.time()

    #os.path.getmtime represents the time the file was last modified
    # also in seconds. Thus, we have an equal base for comparison.
    #Using some dimensional analysis, we need to find out how many
    # second are in a day, as if the difference between currentTime
    # and a file's modification time is less than the dimensional analysis
    # number, it must be less than a day old

    #dimensional analysis: 60 seconds in a minute
    #60 minutes in an hour
    #24 hours in one day
    # 60 * 60 * 24 = 86400
    dimAnalysis = 86400

    #Creating a variable to show how many files were transferred for clarity
    fileTransferNumber= 0
    
    for i in files:
        #We are saying move the files represented by 'i' to their new destination
        print(os.path.getmtime(source + i))

        #establishing our calculation here:
        if currentTime - os.path.getmtime(source + i) < dimAnalysis:
            #Only if we get a success do we move the file!
            shutil.move(source+i, destination)
            fileTransferNumber = fileTransferNumber + 1

    return fileTransferNumber


if __name__ == "__main__":
    pass
