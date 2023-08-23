import sys

def patternMatching(pattern,filename):
    try:
        with open(filename,"r") as file:
            content = file.read()
            lines = content.split(".")
            for i in lines:
                if(i.find(pattern) != -1):
                    print(i)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

if(len(sys.argv) != 3):
    print("Usage: python cat.py <filename>")
else:
    file = sys.argv[1]
    pat = sys.argv[2]
    patternMatching(pat,file)


