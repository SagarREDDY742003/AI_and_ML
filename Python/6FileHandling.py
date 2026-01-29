############ Reading and Writing Files in Python ############

####----WRITE MODE-----######################################

file = open('example.txt', 'w')

# write() - Writing a single string to the file
file.write('Hello, World!\n')
file.write('This is a test file.\n')
file.close()


# Writing multiple lines to a file
lines = ['First line\n', 'Second line\n', 'Third line\n']   
with open('multiple_lines.txt', 'w') as file:
    file.writelines(lines)
# with statement automatically closes the file even if an error occurs


####----READ MODE-----####################################

file = open('example.txt', 'r')
# Reading the contents of the file
content = file.read()
print(content)
file.close()

# read() - Reads the entire file content as a single string
with open('multiple_lines.txt', 'r') as file:
    content = file.read()
    print(content)

# readline() - Reads one line at a time
with open('example.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()

# readlines() - Reads the file line by line into a list
with open('example.txt', 'r') as file:
    content = file.readlines()
    for line in content:
        print(line.strip())


####----APPEND MODE-----####################################

file = open('example.txt', 'a')
file.write('Appending a new line.\n')
file.close()
# Reading the updated file
file = open('example.txt', 'r')
content = file.read()
print(content) # Output the updated content
file.close()

####----READ AND WRITE MODE-----####################################

# w+ mode - Opens a file for both writing and reading. If the file exists, it truncates the file to zero length. If the file does not exist, it creates a new file for reading and writing.
# r+ mode - Opens a file for both reading and writing. The file pointer is placed at the beginning of the file. The file must exist.

with open('read_write.txt', 'r+') as file:
    file.write('This file is opened in read and write mode.\n')
    file.seek(0)  # Move the cursor to the beginning of the file
    content = file.read()
    print(content)
    

####----Exception Handling while working with files-------########################

try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()   
        print(content)
except FileNotFoundError:  # Handles the case when the file does not exist
    print("The file does not exist.") 
except PermissionError:    # Handles the case when there are insufficient permissions to access the file
    print("You do not have permission to access this file.")
except IOError:   # Handles other I/O related errors
    print("An I/O error occurred.")
except Exception as e:  # Catches any other exceptions
    print(f"An unexpected error occurred: {e}")
finally:
    print("Execution completed.")