#Conditional Statements
age = 20
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a minor.")
    
#Looping Constructs
#For Loop - Iterating over a range       
for i in range(5):
    print("Iteration:", i)

#While Loop - Repeating until a condition is met
count = 0
while count < 5:
    print("Count:", count)
    count += 1
    
#Break and Continue - Controlling Loop Execution
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    if i % 2 == 0:
        continue  # Skip even numbers
    print("Odd number:", i)
    
#Try-Except for Error Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("Execution completed.")

# switch-case
def switch_case_example(value):
    match value:
        case 1:
            return "You selected option 1."
        case 2:
            return "You selected option 2."
        case 3:
            return "You selected option 3."
        case _:
            return "Invalid option selected."