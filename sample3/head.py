import sys

def first_five_lines(filename):
    try:
        with open(filename, "r") as file:
            for i in range(5):
                content = file.readlines()
                if not content:
                    break
                print(content)  
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

if len(sys.argv) != 2:
    print("Usage: python head.py <filename>")
else:
    filename = sys.argv[1]
    first_five_lines(filename)