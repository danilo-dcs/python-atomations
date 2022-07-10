import os

from FilesPractice.FilesManager import FilesManager

# FUNCTIONS SUMARY

# os.getcwd() # returns the current workdir
# os.chdir("/home") # changes the current directory to "/home"
# os.path.dirname() # returns the directory path of a path
# os.path.basename() # returns the final component of a path, or the file name
# os.path.abspath() # returns the absolute path of a relative local file
# os.path.isabs() # returns true if the path is absolute
# os.path.isdir() # returns true if the path is a directory
# os.path.isfile()  # returns true if the path indicates a regular file
# os.path.exists() # returns true if the path is a valid path
# os.path.getsize() # gets the size in bytes of a file
# os.path.join() # join 2 paths arguments
# os.listdir() # lists all file and folder names inside a cirectory path
# os.makedirs() # create new folders in the specified relative or absolute paths

def main():
    print("DEALING WITH PATHS") # getting the current working directory

    filesManager = FilesManager()


if __name__ == "__main__":
    main()
