
# Functions - A block of reusable code that performs a specific task.
def add(a, b):
    """Function to add two numbers."""
    return a + b

result = add(5, 3)
print("Addition Result:", result)

# Scope - The region of a program where a variable is accessible.
# Global variable - accessible throughout the module
# local variable - accessible only within the function

# Lifetime - The duration for which a variable exists in memory.
# A local variable exists only while the function is executing.


#---------------------------------------------------------------------------------------------------------------

# Modules - A file containing Python code that can define functions, classes, and variables.

# To create a module, save the following code in a file named 'mymodule.py':
def subtract(a, b):   
    """Function to subtract two numbers."""
    return a - b

# Then, you can import and use it in another file as follows:
# from mymodule import subtract 
# difference = subtract(10, 4)
# print("Subtraction Result:", difference)

# You can also import the entire module:
# import mymodule
# difference = mymodule.subtract(10, 4)
# print("Subtraction Result:", difference)

# Standard Library Modules - Python comes with a rich standard library.
import math 
print("Square root of 16 is:", math.sqrt(16))
import math as m
print("Square root of 9 is:", m.sqrt(9))
from math import sqrt
print("Square root of 25 is:", sqrt(25))

import random   
print("Random number between 1 and 10:", random.randint(1, 10))
import datetime
print("Current date and time:", datetime.datetime.now())