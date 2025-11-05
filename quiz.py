from questions import quiz_questions

print("Welcome to my quiz! Answer each question by typing A, B , C, or D")

score = 0

for q in quiz_questions:
    print("\n" + q ["question"])
    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer(A, B, C, or D):").strip().upper()

    if user_answer == q["answer"]:
        score +=1

    else: 
        print("The answer is wrong. The correct answer is " + q["answer"]) 
    print("Your current score is: " + str(score) + "/" + str(len(quiz_questions)))   

print("\n Quiz complete!")
print("Your final score is " + str(score) + "/" + str(len(quiz_questions)))
print("Great job! Thanks for playing ")


