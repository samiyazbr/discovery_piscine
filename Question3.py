# Guessing game between 1 and 10

import random

number = random.randint(1, 10)

guess = input("Guess a number: ")

if guess == number
    print("Correct!")
elif guess > number:
    print("Too high!")
elif guess < number:
    print("Too low!")
else
    print("Invalid")

tries = 0
while tries < 3
    guess = input("Try again: ")
    tries += 1
    if guess = number
        print("You got it!")
        break

if tries == 3
print("Out of tries!")

print("Game over"
print(result)
