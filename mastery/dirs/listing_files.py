# Python program to explain os.listdir() method
	
# importing os module
import os

from mastery.dirs.making_dir import getFileDir

# Get the list of all files and directories
# in the root directory

dirPath = getFileDir(__file__)
dir_list = os.listdir(os.path.dirname(dirPath))

print("Files and directories in '", path, "' :")

# print the list
print(dir_list)
