# Guessing game between 1 and 10

import random

number = random.randint(1, 10)

guess = input("Guess a number: ")   # ⚠️ Logical: input is str, not int

if guess == number                  # ❌ Missing colon
    print("Correct!")
elif guess > number:
    print("Too high!")
elif guess < number:
    print("Too low!")
else
    print("Invalid")                # ❌ Missing colon after else

tries = 0
while tries < 3                     # ❌ Missing colon
    guess = input("Try again: ")
    tries += 1
    if guess = number               # ❌ Using = instead of ==; ❌ Missing colon
        print("You got it!")
        break

if tries == 3
print("Out of tries!")              # ❌ Missing colon and indentation

print("Game over"                   # ❌ Missing closing parenthesis
print(result)                       # ❌ Undefined variable (NameError)
