from mathematicalOperations import add, subtract, multiply, divide

num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))

print("select the option")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Divison")
print("5. Exit")

while(True):
    
    choice = int(input("Enter the choice from (1/2/3/4/5): "))
    
    if choice in (1,2,3,4,5):
        if choice == 1:
            print(f"Addition of {num1} and {num2} is {add(num1,num2)}")
        elif choice == 2:
            print(f"Subtraction of {num1} and {num2} is {subtract(num1,num2)}")
        elif choice == 3:
            print(f"Multiplication of {num1} and {num2} is {multiply(num1,num2)}")
        elif choice == 4:
            print(f"Divison of {num1} and {num2} is {divide(num1,num2)}")
        elif choice == 5:
            print("Thank You :)")
            exit()
    else:
        print("Invalid choice try again")