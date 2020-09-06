types_of_people = 10
x = f"There are {types_of_people} types of people." # string formatted with variable

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}." # string with formatted variable

print(x)
print(y)

print(f"I said: {x}") # a foratted string with a formated string inside
print(f"I also said: '{y}'") # a foratted string with a formated string inside

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious)) # add the variable into the string using the .format syntax (method?)

w = "This is the left side of..."
e = "a string with a right side."

print(w + e) # the + sign concatenates strings
