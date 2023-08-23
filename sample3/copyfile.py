import sys

def copyFile(sfile,dfile):
    try:
        with open(sfile,"r") as sourcefile:
            with open(dfile,"a") as destfile:
                content = sourcefile.read()
                destfile.write(content)
                print("Success")
    except:
        print("An Error Occured")

if(len(sys.argv) != 3):
    print("Error")
else:
    sofile = sys.argv[1]
    desfile = sys.argv[2]
    copyFile(sofile,desfile)


    