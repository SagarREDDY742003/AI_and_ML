

def reverse_string(str):
    return str[::-1]

def is_palindrome(str):
    return str == reverse_string(str)

def count_vowels(str):
    return sum(1 for char in str.lower() if char in 'aeiou')
        