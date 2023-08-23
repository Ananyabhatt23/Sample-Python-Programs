import sys
import os

# def largestFile():
#     dir = os.path.getsize("E:\\SVM Documents\\1Paper.pdf")
#     print(dir//1024)
# largestFile()

def largestFileInDir(dirpath):
        mydict = {}
        for i in os.listdir(dirpath):
            # print(os.path.getsize(dirpath + "\\" + i)//1024)
            mydict[os.path.getsize(dirpath + "\\" + i) //1024] = dirpath + "\\" + i
        mykeys = mydict.keys()
        val = max(mykeys)
        print("In the directory " + dirpath + " the largest file is "+ mydict[val] + " having a size of " + str(val) + " KB")

if len(sys.argv) != 2:
      print("Error")
else:
      foldername = sys.argv[1]
      largestFileInDir(foldername)
        