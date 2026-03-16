import random

user_choice = int(input("Type: \n 0 for rock \n 1 for paper \n 2 for scissor \n Enter your Choice: "))

arr = [0,1,2]

if user_choice in arr:
    
    computer_choice = random.randint(0,2)
    print("Computer Chose: ",computer_choice)

    if computer_choice == user_choice:
        print("It's a draw.")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose.")
    elif computer_choice == 2 and user_choice == 0:
        print("You Win.")
    elif computer_choice > user_choice:
        print("You Lose.")
    elif user_choice > computer_choice:
        print("You Win.")
else:
    print("Enter a valid number.")