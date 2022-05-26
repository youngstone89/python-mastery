# Python program to explain os.mkdir() method

# importing os module
import os

# Directory
directory = "GeeksforGeeks"

# mode
mode = 0o666

def getFileDir(file):
    absPath = os.path.abspath(file)
    curDir  = os.path.dirname(absPath)
    return curDir



# Path
path = os.path.join(getFileDir(__file__), directory)
os.mkdir(path, mode)

