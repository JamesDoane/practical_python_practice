import random

roll = random.randint(1,6)

guess = int(input('guess the dice roll\n'))

if guess == roll:
    print("you got it!")
else:
    print("you suck")