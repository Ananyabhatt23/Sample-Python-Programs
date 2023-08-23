import sys
import os
import datetime

def mostRecentFile(dirpath):
    formatted_time = {}
    for i in os.listdir(dirpath):
        timeValue = os.path.getmtime(dirpath +"\\"+i)
        modifiedtime = datetime.datetime.fromtimestamp(timeValue)
        formatted_time[(modifiedtime.strftime("%Y-%m-%d %H:%M:%S"))] = dirpath +"\\"+i
    result = formatted_time.keys()
    recentFile = max(result)
    print("The recent edited file is " + formatted_time[recentFile] + " on " + str(recentFile))


if len(sys.argv) != 2:
    print("Error")
else:
    foldername = sys.argv[1]
    mostRecentFile(foldername)
        
