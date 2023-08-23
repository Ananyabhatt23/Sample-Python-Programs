import sys
import os

def largeFileInFolder(folderPath,size):
    filesize, format = size.split()
    files = os.listdir(folderPath)
    for i in files:
        if(format == 'KB'):
            if(os.path.getsize(folderPath+"\\"+i)//1024 > int(filesize)):
                print(f'File is {i}')
        if(format == 'MB'):
            if(os.path.getsize(folderPath+"\\"+i)//2048 > int(filesize)):
                print(f'File is {i}')

if len(sys.argv) != 3:
    print("Error")
else:
    pathoffolder = sys.argv[1]
    filesize = sys.argv[2]
    largeFileInFolder(pathoffolder,filesize) 

