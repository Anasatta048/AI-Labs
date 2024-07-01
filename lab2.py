# Lab 2 - Iterative Structures in Python

# While Loop:
# In python, while loop is used to execute a block of statements repeatedly until a given condition is satisfied.
# When the condition becomes false, the line immediately after the loop in the program is executed.

# Example:
count = 0
while count < 3:
    count += 1
    print("Hello Geek")

# Single statement while block:
count = 0
while count == 0: print("Hello Geek"); count += 1

# For in Loop:
# For loops are used for sequential traversal. For example: traversing a list or string or array.

# Example 1: Iterating over a list
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)

# Example 2: Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)

# Example 3: Iterating over a String
print("\nString Iteration")
s = "Geeks"
for i in s:
    print(i)

# Iterating by index of sequences:
# We can also use the index of elements in the sequence to iterate.
# The key idea is to first calculate the length of the list and then iterate over the sequence within the range of this length.

# Example:
print("\nIterating by index")
list = ["geeks", "for", "geeks"]
for index in range(len(list)):
    print(list[index])

# Loop Control Statements:
# Loop control statements change execution from its normal sequence.

# Continue Statement:
# It returns the control to the beginning of the loop.

# Example: Prints all letters except 'e' and 's'
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)

# Break Statement:
# It brings control out of the loop.

# Example: Break the loop as soon it sees 'e' or 's'
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        break
    print('Current Letter :', letter)

# Python Functions
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function. A function can return data as a result.

# Creating a Function
# In Python, a function is defined using the def keyword.

# Example:
def my_function():
    print("Hello from a function")

my_function()

# Parameters
# Information can be passed to functions as parameter.

# Example:
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Default Parameter Value
# Example: If we call the function without parameter, it uses the default value.
def my_function(country="Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Passing a List as a Parameter
# Example: You can send any data types of parameter to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)

# Return Values
# Example: To let a function return a value, use the return statement.
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# Keyword Arguments
# Example: You can also send arguments with the key = value syntax. This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1="Emil", child2="Tobias", child3="Linus")

# Python Classes/Objects
# Python is an object-oriented programming language. Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

# Create a Class
# Example: Create a class named MyClass, with a property named x:
class MyClass:
    x = 5

# Create Object
# Example: Now we can use the class named MyClass to create objects:
p1 = MyClass()
print(p1.x)

# The __init__() Function
# The examples above are classes and objects in their simplest form, and are not really useful in real-life applications.
# To understand the meaning of classes we have to understand the built-in __init__() function.
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created.

# Example: Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)

# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.

# Example: Insert a function that prints a greeting, and execute it on the p1 object:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# Note: The __init__() function is called automatically every time the class is being used to create a new object.
