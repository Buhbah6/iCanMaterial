'''
 Lesson 2 in the IDE: 
 - Variables and Their Behaviour
 - Operators
 - If Statements
 - Else Statements
 - Elif Statements
 - Using Booleans for Logical Statements
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
print(5 + 5) # -> 10

# Subtraction
print(5 - 5) # -> 0

# Multiplication
print(5 * 5) # -> 25

# Division
print(5 / 5) # -> 1.0

# Modulo
print(5 % 5) # -> 0

# Exponent
print(5 ** 5) # -> 3125

# Floor Division
print(15.5 // 2.5) # -> 6


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
print(5 == 5) # -> True

# Inequality
print(5 != 5) # -> False

# Greater Than
print(5 > 5) # -> False

# Less Than
print(5 < 5) # -> False

# Greater Than or Equal To
print(5 >= 5) # -> True

# Less Than or Equal To
print(5 <= 5) # -> True

# Notice how the equality operator is == and not =
# This is because = is already used for assignment
# So if we used = for equality, it would be confusing


### If Statements ###
# If statements are used to check if a condition is true

# Here is the syntax for an if statement:

# if condition:
#     code