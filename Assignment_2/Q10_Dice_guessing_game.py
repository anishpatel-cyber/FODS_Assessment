#Dice Guessing Game

import random

dice = random.randint(1,6)

guess = int(input("Guess the dice value (1-6): "))

if guess == dice:
    print("😊")
elif abs(guess - dice) == 1:
    print("😐")
else:
    print("❌ Wrong! Dice was:", dice)