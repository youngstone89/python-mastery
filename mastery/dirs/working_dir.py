import os


cwd = os.getcwd()

print(cwd)


# Function to Get the current 
# working directory
def current_path():
    print("Current working directory before")
    print(os.getcwd())
    print()


os.chdir('../')

current_path()