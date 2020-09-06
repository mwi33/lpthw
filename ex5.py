my_name = 'Scott Wood'
my_age = 35
my_height = 74
my_weight = 180
my_eyes = "Blue"
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

# convert inches and pounds to centimeters and kilograms

my_height_cm = my_height * 2.54
my_weight_kg = my_weight * 2.2

print(f"My height in cm is {int(my_height_cm)}.")
print(f"My weight in kg is {int(my_weight_kg)}.")
