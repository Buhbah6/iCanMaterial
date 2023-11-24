"""
 Lesson 3 & 4 in the IDE:
    - Lists
    - Intro to Loops
    - For Loops
    - While Loops
    - Nested Loops
    - Break and Continue 
"""

### Lesson 3 ###
### Lists ###
# Lists are a collection of items in a particular order
# Lists are mutable (can be changed)
# Lists are defined by square brackets []
# Lists can contain any data type

# Create a list of names
names = ["John", "Paul", "George", "Ringo"]
print(names)

# Accessing elements in a list
# Lists are zero-indexed -> this mean that each element has a position, and the first element is at position 0
# To access an element in a list, use the name of the list followed by the index of the element in square brackets
print(names[0])

# You can also use negative numbers to access elements in a list
# This starts at the end of the list and goes backwards
print(names[-1])

# You can also use the index of an element to access it
# This is useful if you want to use the index of an element in a list to access another element in a different list
print(names[names.index("Paul")]) # This will print the element at the index of "Paul" in the names list

# Here"s an example of how this can be useful
# Create a list of first names
firstNames = ["John", "Paul", "George", "Ringo"]
# Create a list of last names
lastNames = ["Lennon", "McCartney", "Harrison", "Starr"]

# Make a program to take a first name, and print the last name
print(lastNames[firstNames.index("John")])

# You can also use the index of an element to change it
# This is useful if you want to change an element in a list
names[0] = "John Lennon"

# You can also add elements to a list
# This is useful if you want to add an element to a list
names.append("Yoko Ono")

# You can also insert elements into a list
# This is useful if you want to add an element to a specific position in a list
names.insert(0, "Some other guy")
# You can also remove elements from a list
# This is useful if you want to remove an element from a list
names.remove("Some other guy")

# You can also get the length of a list using the "len()" function
print(len(names))


### Intro to Loops ###
# Loops are used to repeat code
# There are two types of loops in python: for loops and while loops
# In other languages, there are also do-while loops, but python does not have these

# For loops are used to repeat code a specific number of times -> You know how many iterations you need
# While loops are used to repeat code until a condition is met -> You don"t know how many iterations you need

# Here are the examples of the two types of loops
# For loop
i = 0
for i in range(10):
    print(i)

# While loop
i = 0
while i < 10:
    print(i)
    i += 1


# Let"s say we want to print each letter of a person"s name one by one:

name = input("Please enter your first name: ")
i = 0
while i < len(name): # Here we use the "len()" function to get the length of the string
    print(name[i])
    i = i + 1

# Let"s say I want to add 10 numbers together:
val = 0
i = 0
for i in range(10):
    val = val + i # Notice how I don"t just do val + i, we need to reassign the new value to the val variable
print(val)


### Lesson 4 ###

### Nested Loops ###
# With loops, you can add a layer of complexity by repeating blocks of code. This gets even more tricky with "nested loops"

# A nested loop is simply a loop inside of a loop

i = 0
for i in range(10):
    j = 10
    while j >= 0:
        print(i + j)
        j = j - 1
    i = i + 1
    print(" ")


# This code prints a cool pattern
rows = 15
# outer loop
for i in range(1, rows + 1):
    # inner loop
    for j in range(1, i + 1):
        print("*", end=" ") # Adds " " at the end
    print("")


### Continue and break keywords ###


# break ends the loop. It breaks out of the loop
i = 0
for i in range(10):
    if i == 5:
        break
    print(i)
    i = i + 1

# continue skips the rest of the loop and goes to the next interation.
i = 0
while i < 10:
    if i == 5:
        continue
    print(i)
    i = i + 1

### Practice Problems ###

"""
1. Write a Python program to print a multiplication table of a given number. Take user input for the number, and then 
print the number * every number between 0 and 10

2. Write a program that takes the following list, and reverses it.
    ["keyboard", "mouse", "monitor", "PC"]
            should become
    ["PC", "monitor", "mouse", "keyboard"]

3. Print the following pattern using a nested for loop:
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

"""

# Solutions

# 1.
while True:
    user_num = input("Please enter a number, and we'll calculate the 10x multiplication table for that number")
    if user_num.isdigit():
        num = int(user_num)
        for i in range(1, 11):
            print(user_num +" x " + str(i) + " = " + str(num * i))
        break


# 2.
l1 = ["keyboard", "mouse", "monitor", "PC"]
l2 = []
print(l1)

i = len(l1) - 1
while i >= 0:
    l2.append(l1[i])
    i = i - 1
l1 = l2
print(l1)

# 3.
rows = 100
even = False
if rows % 2 == 0:
    half = rows / 2
    even = True
else:
    half = (rows + 1) / 2

for i in range(1, rows + 1):
    if i <= half:
        for j in range(1, i + 1):
            print("*", end=" ")
    elif even:
        for j in range(1, i):
            print("*", end=" ")
        even = False
    else:
        for j in range(1, i - (i - j)):
            print("*", end=" ") 
    print("")