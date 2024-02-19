'''
Lesson 6 and 7 in the IDE: 
- Intro to OOP
- Classes and Objects
- Instance variables and methods
- Class variables and methods
- Practice Problems
'''

## Intro to OOP ##
# OOP: Object Oriented Programming
# OOP is a programming paradigm that uses objects and their interactions to design applications and computer programs
# OOP is based on the concept of objects
# An object is a collection of data (variables) and methods (functions) that act on those data
# Example: A car is an object
# Its data (variables) are: make, model, color, etc.
# Its methods (functions) are: accelerate, brake, etc.
# You can have multiple instances of the same object
# Each instance has its own values for the variables

## Classes and Objects ##
# A class is a blueprint for objects

# Example: Create a class called Person

class Person:
    name = "John"

# Create an object of type Person
p1 = Person()
print(p1.name)

# Example: Create a class called Person, use the __init__() function to assign values for name and age

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an object of type Person
p1 = Person("John", 36)
print(p1.name)
print(p1.age)

# The __init__() function is called automatically every time the class is being used to create a new object
# This is called a constructor function, because it is used to construct objects.
# Every class has a constructor function, even if we do not define it
# If we do not add the __init__() function, Python will add an empty one for us

# To modify properties on an object or to call a method of that object, use the dot notation
# Example: Set the age of p1 to 40

p1.age = 40
print(p1.age)


## Instance Variables and Methods ##
# Instance variables are variables that belong to the object
# In the example above, p1 is an object of type Person, and its instance variables are name and age

# Instance methods are methods that belong to the object
# They only affect the object itself, not the whole class
# here is how you define a method.

def method_name(parameters):
    # method body -> code to be executed
    return # Return statement / or no return statement

def print_word_letters(word):
    for letter in word:
        print(letter)
    return word

# Here is how you call a method
word = print_word_letters("Hello")
print(word)

# In the context of a class here is how you define a method

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_name(self):
        print("My name is:", self.name)

    def say_age(self):
        print("My age is:", self.age)

# Notice the self parameter in the method definition
# The self parameter is a reference to the current instance of the class.
# When the method uses self, it is only affecting the object calling the method.

# Using the person class

p1 = Person("John", 16)
p2 = Person("Jane", 17)

p1.say_name() # My name is: John
p2.say_name() # My name is: Jane


## Class Variables and Methods ##
# Class variables are variables that belong to the class
# They are shared by all instances of the class
# In the example below, all instances of the class Person will have the same class variable greeting

class Person:
    greeting = "Hello"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_greeting(self):
        print(self.greeting)

# Using the person class

p1 = Person("John", 16)
p2 = Person("Jane", 17)

p1.say_greeting() 
p2.say_greeting()

Person.greeting = "Hi" # Change the greeting for all instances of the class
p2.say_greeting()


# Class methods are methods that belong to the class
# They are shared by all instances of the class
# In the example below, all instances of the class Person will have the same class method say_greeting

class Person:

    greeting = "Hello"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def say_greeting(cls):
        print(cls.greeting)

    @classmethod
    def change_greeting(cls, new_greeting):
        cls.greeting = new_greeting

# Using the person class

p1 = Person("John", 16)
p2 = Person("Jane", 17)

p1.say_greeting()
p2.say_greeting()

p1.change_greeting("Hi") # Change the greeting for all instances of the class
p2.say_greeting()

# Notice the cls parameter in the method definition
# The cls parameter is a reference to the class itself.
# It works the same way as the self parameter, but instead of accessing the instance of the class, it accesses the class itself.


## Practice Problems ##

# 1. Create a class called Dog
# The class should have the following properties:
# name, age, breed, color
# The class should have the following methods:
# bark, eat, sleep, run
# Create 2 dogs and print their name, age, breed, and color
# Call the methods on both dogs


# 2. Create a class called Car
# The class should have the following properties:
# brand, model, color, sizeOfGasTank, gasLevel
# The class should have the following methods:
# drive, fillGas
# for the drive method, take a parameter for distance in km. assume each km consumes 1 liter of gas -> If there is not enough gas, print "Not enough gas!" and don't drive
# for the fillGas method, take a parameter for liters of gas added to tank -> Make sure gas level doesn't exceed tank capacity