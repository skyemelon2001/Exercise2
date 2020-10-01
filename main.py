import random
target_num, guess = random.randint(1, 10), 0

guess = int(input("Guess a number between 1 and 10: "))

if (target_num != guess):
    print("You guessed incorrectly")
else:
    print("You got it right, congratulations!")
