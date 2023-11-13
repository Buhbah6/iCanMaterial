'''
 Lesson 3 & 4 in the IDE:
    - Lists
    - Intro to Loops
    - For Loops
    - While Loops
    - Nested Loops
    - Break and Continue 
'''

### Lesson 3 ###
### Lists ###
# Lists are a collection of items in a particular order
# Lists are mutable (can be changed)
# Lists are defined by square brackets []
# Lists can contain any data type

# Create a list of names
names = ['John', 'Paul', 'George', 'Ringo']
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
print(names[names.index('Paul')]) # This will print the element at the index of 'Paul' in the names list

# Here's an example of how this can be useful
# Create a list of first names
firstNames = ['John', 'Paul', 'George', 'Ringo']
# Create a list of last names
lastNames = ['Lennon', 'McCartney', 'Harrison', 'Starr']

# Make a program to take a first name, and print the last name
print(lastNames[firstNames.index('John')])

# You can also use the index of an element to change it
# This is useful if you want to change an element in a list
names[0] = 'John Lennon'

# You can also add elements to a list
# This is useful if you want to add an element to a list
names.append('Yoko Ono')

# You can also insert elements into a list
# This is useful if you want to add an element to a specific position in a list
names.insert(0, 'Some other guy')

# You can also remove elements from a list
# This is useful if you want to remove an element from a list
names.remove('Some other guy')


### Intro to Loops ###
# Loops are used to repeat code
# There are two types of loops in python: for loops and while loops
# In other languages, there are also do-while loops, but python does not have these

# For loops are used to repeat code a specific number of times -> You know how many iterations you need
# While loops are used to repeat code until a condition is met -> You don't know how many iterations you need

# Here are the examples of the two types of loops
# For loop
for i in range(10):
    print(i)

# While loop
i = 0
while i < 10:
    print(i)
    i += 1


### Lesson 4 ###