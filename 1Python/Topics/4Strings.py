
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
print(" ".join(["Hello", "World"])) # "Hello World"
print("-".join(["Hello", "World"])) # "Hello-World"

# find() - Returns the lowest index of the substring if found, otherwise -1.
print(s.find("World"))    # 8

# format() - Formats specified values in a string.
print("Hello, {}".format("Alice"))  # "Hello, Alice"


############################## String Manipulation ##############################

# Concatenation - You can concatenate strings using the + operator.
s1 = "Hello"
s2 = "World" 
s3 = s1 + " " + s2
print(s3)  # Hello World

# Repetition - You can repeat strings using the * operator.
s = "Ha" * 3    
print(s)  # HaHaHa

# Membership Testing - You can check if a substring exists within a string using the in keyword.
s = "Hello World"
print("World" in s)  # True
print("world" in s)  # False

# String Length - You can get the length of a string using the len() function.
s = "Hello"
print(len(s))  # 5

# String Comparison - You can compare strings using comparison operators (==, !=, <, >, <=, >=).
s1 = "apple"    
s2 = "banana"
print(s1 < s2)  # True Explanation: Strings are compared lexicographically (dictionary order).
print(s1 == s2) # False
print(s1 != s2) # True
print(s1 > s2)  # False
print(s1 <= s2) # True
print(s1 >= s2) # False

# Escape Sequences - You can use escape sequences to include special characters in strings.
s = "Hello\nWorld"  # \n is a newline character
print(s)  # Hello
          # World
s = "He said, \"Hello World!\""  # \" is used to include double quotes in the string
print(s)  # He said, "Hello World!"

# formatting with f-strings (Python 3.6+)
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")  # My name is Alice and I am 30 years old.
# Old style formatting
print("My name is %s and I am %d years old." % (name, age))  # My name is Alice and I am 30 years old.
# Using str.format()
print("My name is {} and I am {} years old.".format(name, age))  # My name is Alice and I am 30 years old.
# Using format with positional and keyword arguments
print("My name is {0} and I am {1} years old.".format(name, age))  # My name is Alice and I am 30 years old.
print("My name is {name} and I am {age} years old.".format(name=name, age=age))  # My name is Alice and I am 30 years old.  
# Padding and alignment
print(f"{'Name':<10} {'Age':>5}")  # Name      Age
print(f"{name:<10} {age:>5}")      # Alice      30


##################### Regular Expressions for Pattern Matching ##########################
import re

# Example: Find all occurrences of the word "cat" in a string
text = "The cat sat on the mat with another cat."

search = re.search(r'cat', text)
print(search.group())  # cat

matches = re.findall(r'cat', text)
print(matches)  # ['cat', 'cat']

# Example: Replace all occurrences of "cat" with "dog"
new_text = re.sub(r'cat', 'dog', text)
print(new_text)  # The dog sat on the mat with another dog.

text = "My phone number is 123-456-7890."
pattern = r'\d{3}-\d{3}-\d{4}'
match = re.search(pattern, text)
if match:
    print("Phone number found:", match.group())  # Phone number found: 123-456-7890
else:
    print("No phone number found.")

# Example: Validate an email address
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email = "test@example.com"
if re.match(email_pattern, email):
    print("Valid email address.")
else:
    print("Invalid email address.")
# Valid email address.