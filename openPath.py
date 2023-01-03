import subprocess, sys, os
#Got load paths to work
#Now just need to create addPath
"""
paths = {"python projects": "F:\\Code\MyPythonScripts\\",
         "cheat tables": "F:\\Tools\\Cheat Tables\\",
         "python 39": "C:\\Users\\brand\\AppData\\Local\Programs\\Python\\Python39",
         "python 37": "C:\\Users\\brand\\AppData\\Local\\Programs\\Python\\Python37\\",
         "steam games": "F:\\Steam\\steamapps\\common",
         "ds3 backups": "F:\\Backups\\ds3\\",
         "ds3": "F:\\Steam\\steamapps\\common\\DARK SOULS III\\Game",
         "passwords": "F:\\Important Documents\\passwords.txt",
         "equalizer": "F:\\Tools\\Equalizer APO\\config",
         "pictures": "C:\\Users\\brand\\OneDrive\\Pictures\\Saved Pictures\\ToBeUsedPictures\\SuperRes\\",
         "videos": "F:\\Videos\\OBS",
         "moonscraper": "F:\\Tools\\Moonscraper\\Moonscraper Chart Editor.exe",
         "mycharts": "F:\\Song Charts",
         "clone hero songs": "F:\\Games\\Clone Hero\\songs\\",
         "code": "F:\\Code\\",
         "tools": "F:\\Tools\\"}
"""

paths = {}
current_directory = "F:\\Code\\MyPythonScripts\\OpenPath\\"
def loadPaths():
    pathsFile = open("paths.txt","r")
    for line in pathsFile.readlines():
        split = line.split(",")
        name = split[0]
        path = split[1].split("\n")[0]
        paths[name] =path
    print(paths)
    
def main():
    loadPaths()
    if len(sys.argv) > 1:
        desiredPath = sys.argv[1]
        findPath(desiredPath)
    else:
        # Draw instructions
        header = "AVAILABLE PATHS".center(75, "=")
        print(header)
        for i in paths.items():
            printString = (i[0].ljust(25, "=") + i[1])
            print(printString)
        desiredPath = input("Where to: ")
        findPath(desiredPath)
        print("Took command")


# Find Path
def findPath(desiredPath):
    print("Hello")
    if desiredPath in list(paths.keys()):
        print("Valid path")
        print(paths[desiredPath])
        if os.path.isdir(paths[desiredPath]):
            print("Is dir")
            print(str(paths[desiredPath]))
            subprocess.Popen('explorer ' + str(paths[desiredPath]))
            return
        elif os.path.isfile(paths[desiredPath]):
            print("Is file")
            os.startfile(paths[desiredPath])
            return
            # subprocess.Popen(str(paths[desiredPath]))
        else:
            print("neither file nor dir")
            return
    else:
        print("File not found. Exiting.")
        return


main()

#
#   End of main body
#   Main


#
