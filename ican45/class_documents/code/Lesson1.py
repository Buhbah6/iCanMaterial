'''
 Lesson 1 in the IDE: 
 - Data Types
 - How Data Types interact 
 - Converting from one data type to another
 - Variables
 - Functions / Methods
 - Practice problems
 '''

### Data Types ###

# Strings - Strings are a sequence of characters
# As stated in the lecture, strings are typically represented within double quotes
print("Hello World!")
print("John")
# They can also be put in single quotes:
print('Hello World!')
# But for the sake of this class, I'd like you to use double quotes for strings

# Integers - Integers are whole numbers
print(5)
print(10)
# No matter what, and integer will never have a decimal point

# Floats - Floats are numbers with decimal points
print(5.0)
print(10.5)

# Booleans - Booleans are either True or False
print(True)
print(False)
# Booleans will be very important when we get to if/else statements, and other logic statements

# Chars - Chars are a single character
print('a')
print('b')
# As you can see chars are represented with single quotes
# You can also use double quotes, but I'd like you to use single quotes for chars


### How Data Types interact ###

# You can add strings together
print("Hello" + "World") # -> "HelloWorld"

# You can add ints together
print(5 + 5) # -> 10

# You can add floats together
print(5.0 + 5.0) # -> 10.0

# When you add chars together, you get a string
print('a' + 'b') # -> "ab"

# Now what do you think we'll get when we do this?
print(5 + 5.0) # -> ?
# or this?
print("1" + "2") # -> ?

# The second one is strange, because it returns "12" instead of 3
# This is because when you add two strings together, it concatenates them
# Concatenation is when you put two strings together
# So "1" + "2" = "12"
# or "Hello" + "World" = "HelloWorld"


### Converting from one data type to another ###

# Sometimes you'll want to convert from one data type to another
# For example, if you want to add two numbers together, but one is a string
# You'll need to convert the string to an int or float
print(5 + int("5")) # -> 10
print(5 + float("5")) # -> 10.0
# To convert from one data type to another, you just put the data type you want to convert to in front of the value
# So int("5") converts the string "5" to an int

# Here are all the conversion methods:
# str() - Converts to a string
# int() - Converts to an int
# float() - Converts to a float
# bool() - Converts to a boolean
# chr() - Converts to a char

# Try converting these values to different data types
# "5" -> int
# "5.0" -> float
# 5 -> string
# 5.0 -> string
# True -> string
# True -> int

# Some will behave in ways you don't expect
# Try:
print(bool("False")) # -> ?
# This is because "False" is a string, and all strings are True

## Variables ##
# Variables are a way to store data
# You can think of them as a box that holds a value
name = "Mr. Nadeau"
age = 117
first_letter = 'a'
# You can name variables anything you want, but there are some rules:
# - They can't start with a number
# - They can't have spaces
# - They can't have special characters
# - They can't be a reserved word (like print, or int)
# - And in python, we traditionally use snake_case for variable names
# - snake_case is when you use underscores to separate words

# You can also change the value of a variable
name = "Billibob Joe"
# if I print name, it will now be "Billibob Joe"


## Functions / Methods ##

# Functions are blocks of code that do something
# They can take in values, and return values
# For example, the print function takes in a value, and prints it to the console
# The input function takes in a value, and returns the user's input
# Try this:
name = input("What is your name?")
print("Hello " + name + "!")


### Practice Problems ### -> Try to do these on your own, but if you get stuck, feel free to ask for help
'''
1. Write a program that asks the user for their first name, then their last name, and then prints "Hello <first name> <last name>!"

2. Write a program that asks the user for their age, and then prints "You are <age> years old!"

3. Write a program that asks the user for two numbers, and then prints the sum, product, quotient, and difference of those numbers
    # Print the results like this: "Sum: <sum>, Product: <product>, Quotient: <quotient>, Difference: <difference>"

4. Write a program that asks the user for a number, and then prints the number squared
'''

# Solutions

# 1.
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
print("Hello " + first_name + " " + last_name)

# 2.
age = input("What is your age? ")
print("You are " + age + " years old!")

# 3.
num1 = int(input("Please enter the first integer"))
num2 = int(input("Please enter the second integer"))
print("Sum: " + str(num1 + num2))
print("Product: " + str(num1 * num2))
print("Quotient: " + str(num1 / num2))
print("Difference: " + str(num1 - num2))

# 4.
num = int(input("Please enter a number"))
print("The square of " + str(num) + " is " + str(num * num))

