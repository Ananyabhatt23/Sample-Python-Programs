import sys

def print_file_contents(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

if len(sys.argv) != 2:
    print("Usage: python cat.py <filename>")
else:
    filename = sys.argv[1]
    print_file_contents(filename)




                    

