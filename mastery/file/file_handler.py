# Python program to demonstrate
# seek() method


import os


scriptFilePath = os.path.abspath(__file__)
dirName = os.path.dirname(scriptFilePath)
filePath = os.path.join(dirName,"GfG.txt")

# Opening "GfG.txt" text file
f = open(filePath, "r")

# Second parameter is by default 0
# sets Reference point to twentieth
# index position from the beginning
f.seek(20)

# prints current position
print(f.tell())

print(f.readline())
f.close()
