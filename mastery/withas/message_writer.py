import os
from file import curDir





# a simple file writer object
  
class MessageWriter(object):
    def __init__(self, file_name):
        print('init')
        self.file_name = file_name
      
    def __enter__(self):
        print('enter')
        self.file = open(self.file_name, 'w')
        return self.file
  
    def __exit__(self):
        print('exit')
        self.file.close()
  
# using with statement with MessageWriter
  
filePath = os.path.join(curDir,'message.txt')
with MessageWriter(filePath) as xfile:
    xfile.write('hello world')