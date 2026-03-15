from database import question_bank,options
print("********************************************")
print("Welcome to My Quiz Game!!!")

score = 0
answered = 0
for question_num in range(len(question_bank)):
    print("**********************************************")
    print(question_bank[question_num]['text'])
    for i in options[question_num]:
        print(i)
    
    guess = input("Enter your answer(A/B/C/D): ").upper()
    answered +=1
    if guess == question_bank[question_num]['answer']:
        print("Correct Answer")
        score+=1
    else:
        print("Incorrect Answer")
        print("Correct answer is",question_bank[question_num]['answer'])
        
    print(f"Your current score: {score}/{answered}")

print("********************************************************")
print(f"Your have given: {score} correct answers.")
print(f"Your final score is: {(score/answered)*100}%")
    
