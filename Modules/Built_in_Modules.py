# What is Modules.py?
# Modules.py is a Python file that typically contains a collection of functions, 
# classes, and variables that can be imported and used in other Python scripts. 
# It serves as a way to organize code into reusable components, making it easier 
# to manage and maintain larger projects. Modules can be built-in or user-defined, 
# allowing developers to create their own libraries of code for specific tasks or functionalities.

# Using Built-in Modules
import math
print("Square root of 16 is:", math.sqrt(16))
print(math.pi)

# import only what you need
from math import sqrt, pi
print(sqrt(25))
print(pi)

# Rename a module (alias)
import math as m
print(m.factorial(5))


