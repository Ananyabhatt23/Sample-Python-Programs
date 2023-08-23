import sys

def sumOfNumInFile(filename):
    try:
        with open(filename,"r") as file:
            sum = 0
            content = file.read()
            num_list = content.split(",")
            print(num_list)
            for i in range(len(num_list)+1):
                sum =  int(i) + sum
            print(sum)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

if len(sys.argv) != 2:
    print("Usage: python cat.py <filename>")
else:
    filename = sys.argv[1]
    sumOfNumInFile(filename)
