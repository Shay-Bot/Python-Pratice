import random

print("Welcome to the Number Guessing Game!!")
game = input("Do you want the Play the Game? (y/n): ")
r = random.randint(1,10)
score = 0

if game != "y":
    print("Next Time :( ")
    quit()

print("Yahoo!! Lets Continue ")
print("Enter a number Between 1 to 10")

while True:
    guess = input("Enter a Number: ")

    if guess.isdigit():
        guess = int(guess)
        score += 1

        if guess <= 0 or guess >= 11:
            print("Enter a number Between 1 to 10")
        elif guess > r:
            print("Too High!!!")
        elif guess < r:
            print("Too Low!!!")
        else:
            print("Correct Answer")
            print(f"Guesses it take: {score}")
            break
    else:
        print("Invalid Statement")
