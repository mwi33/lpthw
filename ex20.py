from sys import argv

script, input_file = argv

def print_all(f):
    """Function which prints the contents of the input file."""
    print(f.read())

def rewind(f):
    """Function which returns to the begining of the file."""
    f.seek(0)

def print_a_line(line_count, f):
    """Function which prints only a specific line which is passed
    as an integer"""
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:")

print_all(current_file)

print("No let's rewind, kind of like a tape: \n")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
