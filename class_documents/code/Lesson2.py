'''
 Lesson 2 in the IDE: 
 - Variables and Their Behaviour
 - Operators
 - If Statements
 - Else Statements
 - Elif Statements
 - Using Booleans for Logical Statements
 - Practice Problems
 '''

### Variables and Their Behaviour ###

# Last time we saw that we can assign a value to a variable
# We can also change the value of a variable -> This is called reassignment
name = "John"
print(name)
name = "Jane"
print(name)

# We can also assign multiple variables at once
name, age = "John", 20
print(name, age)

# We can also assign the same value to multiple variables at once
name = age = "John"
print(name, age)

# Notice how the last assignment overwrites the previous one
# This is because the computer reads the code from top to bottom
# So it sees the first assignment, and then the second assignment, and then the third assignment
# So it will assign the value "John" to name, and then it will assign the value "John" to age


### Operators ###

# Operators are symbols that do something to values
# Here are some examples:
# + - * / % ** //
# + is the addition operator -> It adds two values together
# - is the subtraction operator -> It subtracts two values
# * is the multiplication operator -> It multiplies two values together
# / is the division operator -> It divides two values
# % is the modulo operator -> It returns the remainder of a division
# ** is the exponent operator -> It raises a value to a power
# // is the floor division operator -> It divides two values and rounds down to the nearest whole number

# Here are some examples:

# Addition
print(5 + 5)  # -> 10

# Subtraction
print(5 - 5)  # -> 0

# Multiplication
print(5 * 5)  # -> 25

# Division
print(5 / 5)  # -> 1.0

# Modulo
print(5 % 5)  # -> 0

# Exponent
print(5**5)  # -> 3125

# Floor Division
print(15.5 // 2.5)  # -> 6


# We also have Boolean operators
# Boolean operators are used to compare two values
# Here are some examples:
# == != > < >= <=
# == is the equality operator -> It checks if two values are equal
# != is the inequality operator -> It checks if two values are not equal
# > is the greater than operator -> It checks if the first value is greater than the second value
# < is the less than operator -> It checks if the first value is less than the second value
# >= is the greater than or equal to operator -> It checks if the first value is greater than or equal to the second value
# <= is the less than or equal to operator -> It checks if the first value is less than or equal to the second value

# Here are some examples:

# Equality
print(5 == 5)  # -> True

# Inequality
print(5 != 5)  # -> False

# Greater Than
print(5 > 5)  # -> False

# Less Than
print(5 < 5)  # -> False

# Greater Than or Equal To
print(5 >= 5)  # -> True

# Less Than or Equal To
print(5 <= 5)  # -> True

# Notice how the equality operator is == and not =
# This is because = is already used for assignment
# So if we used = for equality, it would be confusing


### If Statements ###

# If statements are used to check if a condition is true

# Here is the syntax for an if statement:

# if condition:
#     code

# If the condition is true, then the code will run
# If the condition is false, then the code will not run

# Here is an example:
if 5 == 5:
    print("5 is equal to 5")

# Notice how the code is indented?
# This is because the code is inside the if statement
# The indentation is used to show that the code is inside the if statement
# If the code is not indented, then it is not inside the if statement

# Here are some more examples:
if 5 != 5:
    print("5 is not equal to 5")

if 5 > 5:
    print("5 is greater than 5")

name = input("What is your name? ")  # This asks the user for their name
if not name.isdigit():  # This checks if the name is not a number
    print(name)  # If the name is not a number, then it will print the name

# Notice how we used the not operator?
# The not operator is used to reverse a Boolean value -> True becomes False and False becomes True
# It acts similarly to the != operator, but it can be used for more than just equality


### Else Statements ###

# Else statements are used to run code if the if statement is false
# Here is the syntax for an else statement:
# if condition:
#     code
# else:
#     code

# Here is an example:
if 5 != 5:
    print("5 is not equal to 5")
else:
    print("5 is equal to 5")

# Notice how the else statement is not indented?
# This is because the else statement is not inside the if statement
# If the else statement was indented, then it would be inside the if statement
# This would cause the else statement to run if the if statement was true

# Here are some more examples:

if 5 > 5:
    print("5 is greater than 5")
else:
    print("5 is not greater than 5")

name = input("What is your name? ")  # This asks the user for their name
if name.isdigit():  # This checks if the name is a number
    print("Your name is a number")  # If the name is a number, then it will print "Your name is a number"
else:  # If the name is not a number, then it will print the name
    print(name)


### Elif Statements ###

# Elif statements are used to check multiple conditions
# Here is the syntax for an elif statement:
# if condition:
#     code
# elif condition:
#     code
# else:
#     code

# Here is an example:
num = 10
if num <= 6:
    print("num is less than or equal to 6")
elif num >= 6:
    print("num is greater than or equal to 6")
else:
    print("num is equal to 6")

# An elif statement can have as many elif statements as you want
# It is also similar in function to an if statement
# The only difference is that an elif statement will only run if the previous if or elif statement is false

# Here are some more examples:

name = input("What is your name? ")  # This asks the user for their name
if name.isdigit():  # This checks if the name is a number
    print("Your name is a number")  # If the name is a number, then it will print "Your name is a number"
elif name == "John":
    print("Your name is John")
else:
    print(name)

num = 10;
if num > 5:
    print("num is greater than 5")
if num < 5:
    print("num is less than 6")
else:
    print("num is equal to 5")

# This example has two if statements, rather than an if statement and an elif statement
# Notice how both if statements run, even though the first one is true
# This is where an elif statement would be useful


### Using Booleans for Logical Statements ###

# Booleans are used to store True or False values
# They are useful for checking if a condition is true
# Here is an example:
is_raining = True
if is_raining:
    print("It is raining")
else:
    print("It is not raining")

# Notice how we didn't have to check if is_raining == True?
# This is because is_raining is already a boolean value
# So we can just check if is_raining is true

# Let's add some complexity to this example:

humidityIndex = 0.5
if humidityIndex > 0.5:
    is_raining = True
elif humidityIndex < 0.5:
    is_raining = False
else:
    print("It may or may not rain")

if is_raining:
    print("It is raining")
else:
    print("It is not raining")

# Let's try another example:

# Say someone wishes to know if they are eligible to vote in Canada
# In Canada, you must be 18 years or older to vote, and you must be a Canadian citizen

age = input("How old are you? ") # Asks the user for their age
is_citizen = input("Are you a Canadian citizen? ") # Asks the user if they are a Canadian citizen

if is_citizen == "Yes" or is_citizen == "yes": # Checks if the user is a Canadian citizen
    is_citizen = True # If the user is a Canadian citizen, then is_citizen is True
else: # If the user is not a Canadian citizen, then is_citizen is False
    is_citizen = False 

if age.isdigit(): # Checks if the user entered a number for their age
    if int(age) >= 18 and is_citizen: # Checks if the user is 18 or older and a Canadian citizen
        print("You are eligible to vote") # If the user is 18 or older and a Canadian citizen, then they are eligible to vote
    elif int(age) >= 18 and not is_citizen: # Checks if the user is 18 or older and not a Canadian citizen
        print("You are not eligible to vote") # If the user is 18 or older and not a Canadian citizen, then they are not eligible to vote
    elif int(age) < 18 and is_citizen: # Checks if the user is younger than 18 and a Canadian citizen
        print("You are not eligible to vote") # If the user is younger than 18 and a Canadian citizen, then they are not eligible to vote
    else: # If the user is younger than 18 and not a Canadian citizen, then they are not eligible to vote
        print("You are not eligible to vote")

# Let's look at a last example:

# Say someone wants to know if they can ride a roller coaster at LaRonde
# Assume the roller coaster has a height requirement of 1.5 meters alone, but there is no height requirement if you are with an adult;

with_adult = input("Are you with an adult? ") # Asks the user if they are with an adult
if with_adult == "Yes" or with_adult == "yes": # Checks if the user is with an adult
    with_adult = True # If the user is with an adult, then with_adult is True
else: # If the user is not with an adult, then with_adult is False
    with_adult = False

height = input("How tall are you? ") # Asks the user for their height
if height.isdigit():
    if float(height) >= 1.5 or with_adult: # Checks if the user is 1.5 meters or taller or with an adult
        print("You can ride the roller coaster")
    else: # If the user is not 1.5 meters or taller and not with an adult, then they cannot ride the roller coaster
        print("You cannot ride the roller coaster")

# Notice how we used the or operator? This accepts two boolean values and returns True if either of them are True

# Look at line 285, we checked to see if the user said yes both in lowercase and uppercase letters.
# luckily for us, python has a function called lower() that converts a string to lowercase letters
# so we could have written line 285 like this:
if with_adult.lower() == "yes":
    with_adult = True

# This is useful because it means we don't have to check for both uppercase and lowercase letters


### Practice Problems ###

'''
1. Write a program that asks the user for their first name, then their last name, and ask which they prefer (first or last).
If they say they prefer first, print "Hello <first name>!". If they say they prefer last, print "Hello <last name>!".

2. Write a program that asks the user for their percentage grade, and display their letter grade. Use the following table to assist you:

Percentage Grade | Letter Grade
80 - 100         | A
70 - 79          | B
60 - 69          | C
50 - 59          | D
0 - 49           | F

3. Every school year has roughly 180 days, prompt the user for the number of days they have missed, and 
print the percentage of days they have missed. If the percentage is higher than 5%, print "You have missed a normal amount of days".
If the percentage is between 5% and 10%, print "You have missed a lot of days". 
If the percentage is higher than 10%, print "You have missed too many days".
'''

# Solutions

# 1.

# 2.

# 3.

# 4.

# Assignment 1 and Quiz 1 announcement





