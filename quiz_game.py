print("Welcome the Quiz Game!!")

playing = input("Want to play the Game( Y/N ): ").lower()
score = 0

if playing == "y":
    print("Okay! Lets Play")
else:
    print("Next Time!!")
    quit()

answer = input("What does IT stands for? ").lower()
if answer == "information technology":
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer :(")

answer = input("What does CS stands for? ").lower()
if answer == "computer science":
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer :(")

answer = input("What does SC stands for? ").lower()
if answer == "system call":
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer :(")
answer = input("What does OS stands for? ").lower()
if answer == "operating system":
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer :(")

answer = input("What does I/O stands for? ").lower()
if answer == "input output":
    print("Correct Answer")
    score += 1
else:
    print("Wrong Answer :(")

print(f"Your Total Score is {score}")