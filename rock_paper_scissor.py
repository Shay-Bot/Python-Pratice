import random

print("Welcome to the Game!!")
game = input("Do you want the Play the Game? (y/n): ")
options = ("rock", "paper", "scissors")
computer_score = 0
user_score = 0

if game != "y":
    print("Next Time :( ")
    quit()

print("Yahoo!! Lets Continue ")

while True:

    computer = random.choice(options)
    user = input("Enter any one of these (rock , paper, scissor, q for quit): ").lower()

    if user == "q":
        break

    if user not in options:
        continue

    if user == computer:
        print("Its a Tie")
    elif user == "rock" and computer == "scissors":
        print("You Won!!")
        user_score =+ 1
    elif user == "paper" and computer == "rock":
        print("You Won!!")
        user_score =+ 1
    elif user == "scissors" and computer == "paper":
        print("You Won!!")
        user_score =+ 1
    else:
        print("Computer Won")
        print(computer)
        computer_score =+ 1

print(f"You Won {user_score}")
print(f"Computer Won {computer_score} times")        
