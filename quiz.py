print("Welcome to the Python Quiz App!")
score = 0

# Question 1
answer1 = input("What is 2 + 2? ")
if answer1 == "4":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 2
answer2 = input("What is the capital of France? ")
if answer2.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print(f"Your final score is: {score} out of 2")
