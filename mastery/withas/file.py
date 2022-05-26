import os

absPath = os.path.abspath(__file__)
curDir  = os.path.dirname(absPath)
filePath = os.path.join(curDir, 'example.txt')

with open(filePath,'w') as file:
    file.write('hello world!')