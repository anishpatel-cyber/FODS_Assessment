import random

number = random.randint(1,50)

attempts = 7

for i in range(attempts):
    guess = int(input("Guess the number: "))

    if guess == number:
        print("Correct!")
        break
    elif guess > number:
        print("Too High")

    else:
        print("Too Low")
else:
    print("Better Luck next time!")