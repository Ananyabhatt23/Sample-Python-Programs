import sys
import os

def filesOnly(dirPath):
    for i in os.listdir(dirPath):
        if(os.path.isdir(dirPath+"\\"+i)):
            continue
        print(i)

if len(sys.argv) != 2:
    print("Error")
else:
    folderPath = sys.argv[1]
    filesOnly(folderPath)