# Best practices for writing Pythonic code
# 1. Use meaningful variable and function names
def calculate_area(radius):
    """Calculate the area of a circle given its radius."""
    import math
    return math.pi * radius ** 2
# 2. Follow PEP 8 style guide
def print_area(radius):
    """Print the area of a circle with the given radius."""
    area = calculate_area(radius)
    print(f"The area of a circle with radius {radius} is {area:.2f}")
# 3. Use list comprehensions for concise code
def get_even_numbers(numbers):
    """Return a list of even numbers from the given list."""
    return [num for num in numbers if num % 2 == 0]
# 4. Handle exceptions gracefully
def safe_divide(a, b):
    """Divide two numbers and handle division by zero."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
# 5. write modular code with functions and classes
class Circle:
    """A class to represent a circle."""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        """Calculate the area of the circle."""
        return calculate_area(self.radius)
    
    def print_area(self):
        """Print the area of the circle."""
        print_area(self.radius)
# Example usage
if __name__ == "__main__":
    circle = Circle(5)
    circle.print_area()
    
    numbers = [1, 2, 3, 4, 5, 6]
    even_numbers = get_even_numbers(numbers)
    print(f"Even numbers: {even_numbers}")
    
    result = safe_divide(10, 0)
    print(result)
# 6. Avoid redundant code; leverage python's built-in functions and libraries
def summarize_numbers(numbers):
    """Return the sum and average of a list of numbers."""
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0
    return total, average
# Example usage of summarize_numbers
if __name__ == "__main__":
    nums = [10, 20, 30, 40, 50]
    total, avg = summarize_numbers(nums)
    print(f"Total: {total}, Average: {avg}")


####-----LIST COMPREHENSION-------###################################

# List comprehension is a concise way to create lists in Python.
# It consists of brackets containing an expression followed by a for clause, 
# and can include optional if clauses to filter items.

# Example: Create a list of squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")  # Output: Squares: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Example: Create a list of even numbers from 0 to 19
even_numbers = [x for x in range(20) if x % 2 == 0]
print(f"Even Numbers: {even_numbers}")  # Output: Even Numbers: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

####-----LAMBDA FUNCTIONS-------#########################################

# Lambda functions are small anonymous functions defined with the lambda keyword.
# They can take any number of arguments but can only have one expression.
# lamda arguments: expression

# Example: A lambda function to add two numbers
add = lambda x, y: x + y
result = add(5, 3)
print(f"Result of adding 5 and 3: {result}")  # Output: Result of adding 5 and 3: 8

# map() - Applies a function to all items in an input list (or any iterable).
numbers = [1, 2, 3, 4, 5]   
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Squared Numbers using map: {squared_numbers}")  # Output: Squared

# filter() - Filters items out of an input list (or any iterable) based on a function that returns True or False.
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even Numbers using filter: {even_numbers}")  # Output: Even Numbers using filter: [2, 4]

# reduce() - Applies a rolling computation to sequential pairs of values in a list (or any iterable).
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(f"Product of all numbers using reduce: {product}")  # Output: Product of all numbers using reduce: 120

######----PYTHON OS AND SYS MODULES-----#######################################

####-- OS Module - The os module in Python provides a way of using operating system-dependent functionality like reading or writing to the file system, managing directories, and handling environment variables.
import os

# Create a new directory
new_directory = "test_directory"
if not os.path.exists(new_directory):
    os.mkdir(new_directory)
    print(f"Directory '{new_directory}' created.")
else:
    print(f"Directory '{new_directory}' already exists.")
    
# Get the current working directory
current_directory = os.getcwd()
print(f"Current Working Directory: {current_directory}")

# List files and directories in the current directory
files_and_dirs = os.listdir(current_directory)
print(f"Files and Directories: {files_and_dirs}")

# Remove the created directory
os.rmdir(new_directory)

####-- SYS Module - provides access to system-specific parameters and functions.
import sys
print(f"Python Version: {sys.version}")
print(f"Platform: {sys.platform}")
print(f"Command Line Arguments: {sys.argv}")
