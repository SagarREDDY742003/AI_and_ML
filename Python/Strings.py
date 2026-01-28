
#-----------STRINGS IN PYTHON------------------#

# slicing - it returns a substring by specifying a start index and an end index. [start:end:step]
def reverse_string(s):
    return s[::-1]

s = "GeeksforGeeks"
print(s[1:4])    # characters from index 1 to 3
print(s[:3])     # from start to index 2
print(s[3:])     # from index 3 to end
print(s[::-1])   # reverse string

#String Immutability - Strings in Python are immutable; you cannot change them in place.
s = "Hello" 
# s[0] = 'h'  # This will raise an error
# Instead, create a new string
s = 'h' + s[1:]
print(s)  # hello

# Deleting a String - You can delete a string variable using the del statement.
s = "Hello World"
del s

# Updating a String - You can update a string by creating a new string.
s = "Hello"
s = s + " World"
print(s)  # Hello World

# String Iteration - Strings are iterable; you can loop through characters one by one.
s = "Hello"
for char in s:
    print(char)
    
    
#------------------String Methods-------------------------------
# Common string methods include lower(), upper(), strip(), replace(), split(), join(), find(), and format().
s = "  Hello World  "

# lower() - Converts all characters to lowercase.
print(s.lower())          # hello world

# upper() - Converts all characters to uppercase.
print(s.upper())          # HELLO WORLD

# strip() - Removes leading and trailing whitespace.
print(s.strip())          # "Hello World"

# replace() - Replaces occurrences of a substring with another substring.
print(s.replace("World", "There"))  # "  Hello There  "

# split() - Splits the string into a list of substrings based on a delimiter (default is whitespace).
print(s.split())          # ['Hello', 'World']

# join() - Joins a list of strings into a single string with a specified delimiter.
print("-".join(["Hello", "World"])) # "Hello-World"

# find() - Returns the lowest index of the substring if found, otherwise -1.
print(s.find("World"))    # 8

# format() - Formats specified values in a string.
print("Hello, {}".format("Alice"))  # "Hello, Alice"