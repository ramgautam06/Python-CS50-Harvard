# Ask user for mame 
name = input("What's your name? ")
print(f"My name is {name}")

# Capitalize first and last name only 
fullname = input("What's your full name? ")
first,last = [var.title() for var in fullname.split()]
print(f"My name is {first} {last}")

# Capitalize multiple middle names 
longname = input("What's your long name? ")
capitalize_longname = " ".join([var.title() for var in longname.split()])
print(f"Long name is {capitalize_longname}")