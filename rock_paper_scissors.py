import random


def rps(bot_name, player_name):
    # Welcome the user to the game
    print("Welcome to rock, paper, scissors. Good luck!")
    # Make a choice for the computer player
    computer_choice = random.choice(["r", "p", "s"])

    # Get a choice from the user
    player_choice = input("Rock (r), Paper (p) or Scissors (s)? ")

    # Printing what the computer chooses
    print(f"The computer chooses {computer_choice}")
    
    # Compare the user and computer choice
    # Print the right message, based on the choices
    if (computer_choice == "r" and player_choice == "p"):
        print(f"Paper covers Rock, {player_name} wins")

    elif (computer_choice == "p" and player_choice == "r"):
        print(f"Paper covers Rock, {bot_name} wins")

    elif (computer_choice == "p" and player_choice == "s"):
        print(f"Scissors cut Paper, {player_name} wins")

    elif (computer_choice == "s" and player_choice == "p"):
        print(f"Scissors cut Paper, {bot_name} wins")

    elif (computer_choice == "s" and player_choice == "r"):
        print(f"Rock Smashes Scissors, {player_name} wins")

    elif (computer_choice == "r" and player_choice == "s"):
        print(f"Rock smashes Scissors, {bot_name} wins")

    elif computer_choice == player_choice:
        print("It's a draw")