import sys
import os

def listDirectory(filepath):
    for i in os.listdir(filepath):
        print(i)

if len(sys.argv) == 2:
    folderPath = sys.argv[1]
    listDirectory(folderPath)
elif len(sys.argv) == 1:
    enteredPath = "E:\\Data Structures and algorithms"
    listDirectory(enteredPath)
else:
    print("USAGE: python <python file> <directory path>")


