import sys

def count_lines_words_chars(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            num_lines = content.count('\n') + 1
            num_words = len(content.split())
            num_chars = len(content)
            print(f"Lines: {num_lines}")
            print(f"Words: {num_words}")
            print(f"Characters: {num_chars}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

if len(sys.argv) != 2:
    print("Usage: python cat.py <filename>")
else:
    filename = sys.argv[1]
    count_lines_words_chars(filename)