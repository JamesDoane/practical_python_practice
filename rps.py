import random


computer_choice = random.choice(['scissors', 'paper', 'rock'])

user_choice = input("Rock, paper, or scissors?\n").lower()


if computer_choice == user_choice:
    print("TIE")
elif user_choice == 'rock' and computer_choice == 'scissors':
    print("You win")
elif user_choice == 'paper' and computer_choice == 'rock':
    print("You win")
elif user_choice == 'scissors' and computer_choice == 'paper':
    print("You win")
elif user_choice == 'rock' and computer_choice == 'paper':
    print("You lose")
elif user_choice == 'paper' and computer_choice == 'scissors':
    print("You lose")
elif user_choice == 'scissors' and computer_choice == 'rock':
    print("You lose")
