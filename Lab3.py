myString = "This is a string."
print(myString)
print(type(myString))
print(("'") + myString + ("'") + " is of the data type " + str(type(myString)))

# Create two strings and then concatenate them
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

name = input("What is your name? \n")
print(name)

# use multiple variables to format a string
color = input("What is your favorite color? \n")
animal = input("What is your favorite animal? \n")
print("{}, you like a {} {}!".format(name,color,animal))