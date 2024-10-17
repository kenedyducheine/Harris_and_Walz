import os


# Function to Get the current
# working directory
def current_path():
    print("Current working directory before")
    print(os.getcwd())
    print()


# Driver's code
# Printing CWD before
current_path()
os.chdir('/Users/KenedyDucheine/DataspellProjects/Harris_and_Walz')
current_path()

