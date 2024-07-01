# Introduction to AI and Its Application Using Python

# Python basics and syntax

# Comments in Python
# A comment begins with a hash character (#) and ends at the end of the physical line.

# Print a greeting
print("Hello, World!")

# Input / output
user_input = input("Type something to test this out: ")
print(user_input)

# Multiple Statements on a Single Line
a = 5; b = 10; print(a + b)

# Indentation: Python uses indentation to define blocks of code.
# This is a function with proper indentation
def greet(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, World!")

greet("Alice")

# Data types and Type casting
# Python has several built-in data types, including numbers, strings, and lists.

# Numbers
x = 10         # int
y = 3.14       # float
z = 1 + 2j     # complex

print(type(x))
print(type(y))
print(type(z))

# Boolean
flag = True
print(type(flag))

# Strings
message = "Python Tutorial"
print(message)

# String slicing
substring = message[0:6]
print(substring)

# Lists
color_list = ["RED", "Blue", "Green", "Black"]
print(color_list)

# List slicing
sliced_list = color_list[1:3]
print(sliced_list)

# Conditional Statements
a = 10
b = 5
if b < a:
    print("b is less than a")
elif b == a:
    print("b is equal to a")
else:
    print("b is greater than a")

# Example with logical conditions
if a > b and b < a:
    print("Both conditions are true")
