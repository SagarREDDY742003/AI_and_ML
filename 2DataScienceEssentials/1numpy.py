#####----NUMPY (NUMERICAL PYTHON) ----################################

# NumPy is a powerful library in Python used for numerical computing.
# It provides support for arrays, matrices, and a wide range of mathematical functions.

# Performance: NumPy is optimized for performance, making it faster than standard Python lists for numerical operations.
# Ease of Use: NumPy provides a simple and intuitive interface for working with numerical data.
# Integration: NumPy integrates well with other scientific computing libraries in Python, such as SciPy and Matplotlib.

# Importing the NumPy library
import numpy as np  
# Creating NumPy Arrays
array_1d = np.array([1, 2, 3, 4, 5])  # Creating a 1D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])  # Creating a 2D array
print("1D Array:", array_1d)
print("2D Array:\n", array_2d)
#output:
#1D Array: [1 2 3 4 5]
#2D Array:
# [[1 2 3]
# [4 5 6]]

zeros=np.zeros((2, 3))  # Creating a 2x3 array of zeros
print("Zeros Array:\n", zeros)
#output:
#Zeros Array:
# [[0. 0. 0.]
# [0. 0. 0.]]

ones = np.ones((2, 3))  # Creating a 2x3 array of ones
print("Ones Array:\n", ones)
#output:
#Ones Array:
# [[1. 1. 1.]
# [1. 1. 1.]]

identity = np.eye(3)  # Creating a 3x3 identity matrix
print("Identity Matrix:\n", identity)
#output:
#Identity Matrix:
# [[1. 0. 0.]   
# [0. 1. 0.]
# [0. 0. 1.]]

#######--Array Operations--######################################

# Mathematical operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)  # output: [5 7 9] - Element-wise addition
print(a - b)  # output: [-3 -3 -3] - Element-wise subtraction
print(a * b)  # output: [ 4 10 18] - Element-wise multiplication
print(a / b)  # output: [0.25 0.4  0.5 ] - Element-wise division

# sqrt - Calculating the square root of each element
array_1d = np.array([1, 4, 9, 16, 25])
sqrt_array = np.sqrt(array_1d)  # Square root of each element
print(sqrt_array)  #output: [1. 2. 3. 4. 5]

# sum - Calculating the sum of array elements
sum_array = np.sum(array_1d)
print("Sum:", sum_array)
#output:
#Sum: 15

# mean - Calculating the mean of array elements
mean_array = np.mean(array_1d)  # Mean of elements in the array
print("Mean:", mean_array)
#output:
#Mean: 3.0

# arange - Creating an array with a range of values
range_array = np.arange(0, 10, 2)  # Creating an array with values from 0 to 10 with a step of 2
print("Range Array:", range_array)
#output:
#Range Array: [0 2 4 6 8]

# linspace - Creating an array with evenly spaced values
linspace_array = np.linspace(0, 10, 5)  # Creating an array with 5 evenly spaced values between 0 and 10
print("Linspace Array:", linspace_array)
#output:
#Linspace Array: [ 0.   2.5  5.   7.5 10.]

# Broadcasting - Performing operations on arrays of different shapes 
array_a = np.array([1, 2, 3]) # 1*3 array
array_b = np.array([[10], [20], [30]]) # 3*1 array
broadcasted_sum = array_a + array_b  # Broadcasting addition 
print("Broadcasted Sum:\n", broadcasted_sum)
# output:
#Broadcasted Sum:
# [[11 12 13]
# [21 22 23]
# [31 32 33]] 3*3 array

#### Reshaping Arrays #####
array_1d = np.array([1, 2, 3, 4, 5, 6])
reshaped_array = array_1d.reshape((5, 1))  # Reshaping to a 5x1 array
print("Reshaped Array:\n", reshaped_array)
#output:
#Reshaped Array:
# [[1]
# [2]
# [3]
# [4]
# [5]
# [6]]
reshaped_array = array_1d.reshape((2, 3))  # Reshaping to a 2x3 array
print("Reshaped Array:\n", reshaped_array)
#output:
#Reshaped Array:
# [[1 2 3]
# [4 5 6]]
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
reshaped_array_2d = array_2d.reshape((3, 2))  # Reshaping 2D array to 3x2
print("Reshaped 2D Array:\n", reshaped_array_2d)
#output:    
#Reshaped 2D Array:
# [[1 2]
# [3 4]
# [5 6]]

#### Dimension Manipulation - Adding a new axis to an array #####
arr = np.array([1, 2, 3, 4, 5])
expanded_array = arr[:, np.newaxis]  # Adding a new axis to convert 1D to 2D
print("Expanded Array:\n", expanded_array)
#output:
#Expanded Array:
# [[1]
# [2]
# [3]
# [4]
# [5]]

#### Indexing - Accessing elements in a array #####
array_1d = np.array([10, 20, 30, 40, 50])
element = array_1d[2]  # Accessing the third element
print("Element at index 2:", element)
#output:
#Element at index 2: 30
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
element = array_2d[0, 1]  # Accessing element at row 0, column 1
print("Element at (0,1):", element)
#output:
#Element at (0,1): 2

#### Slicing - Extracting subarrays from arrays #####
array_1d = np.array([10, 20, 30, 40, 50])
slice_1d = array_1d[1:4]  # Slicing from index 1 to 3
print("1D Slice:", slice_1d)
#output:
#1D Slice: [20 30 40]
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
slice_column = array_2d[:, 1]  # Slicing the second column
print("Second Column Slice:", slice_column)
#output:
#Second Column Slice: [2 5]
slice_row = array_2d[1, :]  # Slicing the second row
print("Second Row Slice:", slice_row)
#output:
#Second Row Slice: [4 5 6]
slice_subarray = array_2d[0:2, 1:3]  # Slicing a subarray
print("Subarray Slice:\n", slice_subarray)
#output:
#Subarray Slice:    
# [[2 3]
# [5 6]]

#### Random Number Generation #####
random_array = np.random.rand(3, 3)  # Creating a 3x3 array of random numbers
print("Random Array:\n", random_array)
#output:
#Random Array:
# [[0.5488135  0.71518937 0.60276338]
# [0.54488318 0.4236548  0.64589411]
# [0.43758721 0.891773   0.96366276]]