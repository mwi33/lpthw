from sys import argv

script, filepath = argv

filename = open(filepath)

print(filename.read())
