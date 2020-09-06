# imports the argv function from the sys module
from sys import argv

# defines the required argument for argv
script, filename = argv

#creates a file object
txt = open(filename)

# prints the filename passed through the argv function
print(f"Here's your file {filename}:")

# prints the contents of the file object - txt
print(txt.read())

print("Type the filename again:")

# using the input function pass the filename again
file_again = input("> ")

# creates a file object with the filename again
txt_again = open(file_again)

# prints the contens of the file object
print(txt_again.read())
