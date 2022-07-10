import shelve
import shutil
import os

class FilesManager:
    def readTextFile(path: str) -> any:
        file = open(file=path, mode='r')
        content = file.read()
        file.close()
        return content

    def writeTextFile(path: str, text: str) -> None:
        file = open(file=path, mode='w')  # there is append mode 'a', the append mode does not overwrite the original content
        file.write(text+'\n')
        file.close()


# to store structures and datas like dictionaries, lists and others. Shelve files are 
# stored in binary formats like .bak, .dir, .dat

    def readShelveFile(path: str) -> any: 
        file = shelve.open(file=path)
        keys = file.keys()
        values = file.values()
        file.close()
        return keys, values
    
    def copyFile(origin: str, destiny: str) -> None:
        shutil.copy(origin, destiny)

    def moveFile(origin: str, destiny: str) -> None: 
        shutil.move(origin, destiny)

    def deleteFileOs(path: str) -> None:
        os.unlink(path)  # for files

    def deleteFolderOs(path: str) -> None: 
        os.rmdir(path)  # to remove empty folders

    def deleteFolderShutil(path: str) -> None:
        shutil.rmtree(path)  # removes a folder recursivelly with all its ocntent

## To send files to trash instead of deleting them permanenty, check out the library send2trash. 
# Install it with pip3
