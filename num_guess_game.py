import random

def the_game():
    num_to_guess = random.randint(1,100)

    player_name = input("What's your name?\n")

    player_guess = int(input(player_name + ", I'm thinking of a number between 1-100.\nGuess my number:\n"))
    counter = 1

    while player_guess != num_to_guess:
        if player_guess > num_to_guess:
            print("your guess is too high. try again.")
            player_guess = int(input("New guess?\n"))
            counter+=1
        else:
            print("your guess is too low. try again.")
            player_guess = int(input("New guess?\n"))
            counter+=1

    print("Congratulations", str(player_name), "the number was",str(num_to_guess)+ "! It took you",counter,"attempts.")

    repeater = input("Would you like to play again? y/n\n")

    if repeater == "y":
        the_game()

the_game()