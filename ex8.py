#  -  old line - new line below - formatter = "{} {} {} {}"

formatter = "This is the new formatter,which {} can put {} content in differents {} spots {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, True, False))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format("Try your", "own text here", "maybe a stort", "or not"))
