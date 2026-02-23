#-------------DATA STRUCTURES IN PYTHON-------------#

######################### LIST #################################

# List - Ordered, Mutable, Allows Duplicates
# Lists are used to store multiple items in a single variable
# They are ordered, meaning the items have a defined order and can be accessed by their index
# Lists are mutable, allowing modification of elements after creation
# They can contain elements of different data types
# Lists support various methods for adding, removing, and manipulating elements
# They are widely used in applications such as data storage, manipulation, and iteration
# Lists can be created using square brackets [] or the list() constructor
# Lists support slicing, allowing extraction of sublists
# They can be nested, meaning a list can contain other lists as elements such as matrix representation .
# Lists are dynamic in size, allowing them to grow and shrink as needed

# Creating a list
my_list = [1, 2, 3, 4, 5]

my_list.append(6)  # Adding an element at the end
print("List:", my_list)  #Output: [1, 2, 3, 4, 5, 6]

my_list.insert(0, 0)  # Inserting an element at index 0
print("List after Insertion at index 0:", my_list)  #Output: [0, 1, 2, 3, 4, 5, 6]

my_list.extend([99, 100])  # Extending the list with another list
print("List after Extension:", my_list)  #Output: [0, 1, 2, 3, 4, 5, 6, 99, 100]

# Accessing elements
print("First Element:", my_list[0])  #Output: 0
print("Last Element:", my_list[-1])  #Output: 100

# Slicing  [0, 1, 2, 3, 4, 5, 6, 99, 100]
print("Sliced List (index 2 to 5):", my_list[2:6])  #Output: [2, 3, 4, 5]
print("Sliced List (up to index 4):", my_list[:5])  #Output: [0, 1, 2, 3, 4]
print("Sliced List (from index 4):", my_list[4:])  #Output: [4, 5, 6, 99, 100]
print("Sliced List (every 2nd element):", my_list[::2])  #Output: [0, 2, 4, 6, 99]
print("Reversed List:", my_list[::-1])  #Output: [100, 99, 6, 5, 4, 3, 2, 1, 0]

# Modifying List
my_list[0] = 10
print("List after Modification:", my_list)  #Output: [10, 1, 2, 3, 4, 5, 6, 99, 100]

my_list.remove(1)  # Removing element with value 1
print("List after Removal of 1:", my_list)  #Output: [10, 2, 3, 4, 5, 6, 99, 100]

del my_list[0] # Deleting element at index 0
print("List after Deletion at index 0:", my_list)  #Output: [2, 3, 4, 5, 6, 99, 100]

my_list.pop()  # Removing the last element
print("List after Pop:", my_list)  #Output: [2, 3, 4, 5, 6, 99]   
print("Is 4 in List?", 4 in my_list)  #Output: True

my_list.sort()  # Sorting the list
print("Sorted List:", my_list)  #Output: [2, 3, 4, 5, 6, 99]

my_list.reverse()  # Reversing the list
print("Reversed List:", my_list)  #Output: [99, 6, 5, 4, 3, 2]

my_list.clear()  # Clearing the list
print("Cleared List:", my_list)  #Output: []


######################### TUPLE #################################

# Tuple - Ordered, Immutable, Allows Duplicates
# Tuples are similar to lists but cannot be modified after creation
# They are useful for storing fixed collections of items
# Tuples can be used as keys in dictionaries due to their immutability
# They support indexing and slicing like lists
# Tuples are generally more memory efficient than lists
# They are often used to represent data that should not change throughout the program
# Tuples can be created using parentheses () or the tuple() constructor
# They can contain elements of different data types
# Tuples support unpacking, allowing multiple variables to be assigned values from a tuple in a single statement

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
single_Item_tuple=(1,)
print("Tuple:", my_tuple)  #Output: (1, 2, 3, 4, 5)

# Accessing elements
print("First Element:", my_tuple[0])  #Output: 1
print("Last Element:", my_tuple[-1])  #Output: 5

# Slicing
print("Sliced Tuple (index 1 to 3):", my_tuple[1:4])  #Output: (2, 3, 4)
print("Sliced Tuple (up to index 3):", my_tuple[:4])  #Output: (1, 2, 3, 4)
print("Sliced Tuple (from index 2):", my_tuple[2:])  #Output: (3, 4, 5)
print("Sliced Tuple (every 2nd element):", my_tuple[::2])  #Output: (1, 3, 5)
print("Reversed Tuple:", my_tuple[::-1])  #Output: (5, 4, 3, 2, 1)

# Tuples are immutable, so we cannot modify them
# The following line would raise an error
# my_tuple[0] = 10  this line will raise a TypeError

# However, we can concatenate tuples
new_tuple = my_tuple + (6, 7, 8)
print("Concatenated Tuple:", new_tuple)  #Output: (1, 2, 3, 4, 5, 6, 7, 8)


############################ SET #####################################

# Set - Unordered, Mutable, No Duplicates
# all elements in a set are unique and duplicates are automatically removed
# Sets do not maintain any order of elements
# Sets are useful for membership testing and eliminating duplicate entries
# numbers, strings, and tuples can be elements of a set, but lists and dictionaries cannot
# Sets support operations like union, intersection, difference, and symmetric difference

# Creating a set
my_set = {1, 2, 3, 4, 5}
empty_set = set()  # Creating an empty set
print("Set:", my_set)  #Output: {1, 2, 3, 4, 5}

# Adding elements
my_set.add(6)
print("Set after Addition:", my_set)  #Output: {1, 2, 3, 4, 5, 6}
my_set.update([7, 8, 9])  # Adding multiple elements
print("Set after Update:", my_set)  #Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# modifying elements is not applicable as sets are unordered

# Removing elements
my_set.remove(1)
print("Set after Removal of 1:", my_set)  #Output: {2, 3, 4, 5, 6, 7, 8, 9}
# using remove will raise an error if the element is not found
my_set.discard(2)
print("Set after Discard of 2:", my_set)  #Output: {3, 4, 5, 6, 7, 8, 9}
# Using discard does not raise an error if the element is not found
my_set.pop()
print("Set after Pop:", my_set)  #Output: {4, 5, 6, 7, 8, 9}
print("Is element '4' in Set?", 4 in my_set)  #Output: True
my_set.clear()  
print("Cleared Set:", my_set)  #Output: {}

# set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Union of set_a and set_b:", set_a | set_b)  #Output: {1, 2, 3, 4, 5, 6}
print("Intersection of set_a and set_b:", set_a & set_b)  #Output: {3, 4}
print("Difference of set_a and set_b:", set_a - set_b)  #Output: {1, 2}
print("Symmetric Difference of set_a and set_b:", set_a ^ set_b)  #Output: {1, 2, 5, 6}


################################ DICTIONARY ##########################################

# Dictionary - Ordered, Mutable, No Duplicates for keys
# Dictionaries store key-value pairs
# Keys must be unique and immutable (strings, numbers, or tuples)
# Values can be of any data type and can be duplicated
# Dictionaries are useful for fast lookups, data organization, and representing structured data
# Dictionaries support various methods for adding, removing, and accessing elements
# They also support dictionary comprehensions for creating dictionaries in a concise way
# They are widely used in applications such as configuration settings, data representation (e.g., JSON), and caching

# Creating a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Dictionary:", my_dict)  #Output: {'a': 1, 'b': 2, 'c': 3}

# Accessing elements
print("Value for key 'a':", my_dict['a'])  #Output: 1
print("Value for key 'b':", my_dict.get('b'))  #Output: 2
print("Keys:", my_dict.keys())  #Output: dict_keys(['a', 'b', 'c'])
print("Values:", my_dict.values())  #Output: dict_values([1, 2, 3])
print("Items:", my_dict.items())  #Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

# Modifying Dictionary

my_dict['d'] = 4  # Adding a new key-value pair
print("Dictionary after Addition:", my_dict)  #Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

my_dict['a'] = 10  # Modifying an existing key's value
print("Dictionary after Modification:", my_dict)  #Output: {'a': 10, 'b': 2, 'c': 3, 'd': 4}

del my_dict['b']  # Deleting a key-value pair
print("Dictionary after Deletion of key 'b':", my_dict)  #Output: {'a': 10, 'c': 3, 'd': 4}

my_dict.pop('c')  # Removing a key-value pair using pop
print("Dictionary after Pop of key 'c':", my_dict)  #Output: {'a': 10, 'd': 4}
print("Is key 'd' in Dictionary?", 'd' in my_dict)  #Output: True

my_dict.update({'e': 5, 'f': 6})  # Adding multiple key-value pairs
print("Dictionary after Adding multiple key-value pairs:", my_dict)  #Output: {'a': 10, 'd': 4, 'e': 5, 'f': 6}

my_dict.clear()  # Clearing the dictionary
print("Cleared Dictionary:", my_dict)  #Output: {}

# Iterating through a dictionary
my_dict = {'x': 24, 'y': 25, 'z': 26}
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")
    
#Output:
#Key: x, Value: 24
#Key: y, Value: 25
#Key: z, Value: 26

##########################################################################################################