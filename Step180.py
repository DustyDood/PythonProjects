import os
#We start by establishing the path to the folder we want to loop through!

fPath = 'C:\\Users\\Dusty Zoland\\Documents\\GitHub\\Python_Projects\\PythonProjects'



"""
Old code for reference!
#fName = 'HidingDoc.txt'

abPath = os.path.join(fPath, fName)
print(abPath)
"""

#We then list all the contents in the directory established by fPath
dirList = os.listdir(fPath)

#Finally, we loop through the directory.
for x in dirList:
    #We want to find all files ending in .txt!
    if x.endswith(".txt"):
        #for any matches, we use path.join to find the exact location of the file.
        #From there, we can print the full path and the last time it was modified
        targetAcquired = os.path.join(fPath,x)
        print(targetAcquired)
        print(os.path.getmtime(targetAcquired))



