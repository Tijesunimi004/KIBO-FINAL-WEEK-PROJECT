import random


def rps():
# Write your solution below the starter code
# Follow the instructions in the tab to the right
# import random
    player_name = input("Input your name: ")
# Welcome the user to the game
    print("Welcome to rock, paper, scissors. Good luck!")
# Make a choice for the computer player
    word1 = "Rock"
    word2 = "Paper"
    word3 = "Scissors"

    computer_choice = random.choice([word1, word2, word3])
# Get a choice from the user
    player_choice = input("Rock, Paper or Scissors? ")
# Printing what the computer chooses
    print(f"The computer chooses {computer_choice}")
# Compare the user and computer choice
# Print the right message, based on the choices
    if (computer_choice == "Rock" and player_choice == "Paper"):
        print(f"Paper covers Rock, {player_name} wins")
    elif (computer_choice == "Paper" and player_choice == "Rock"):
        print("Paper covers Rock, Computer wins")
    elif (computer_choice == "Paper" and player_choice == "Scissors"):
        print(f"Scissors cut Paper, {player_name} wins")
    elif (computer_choice == "Scissors" and player_choice == "Paper"):
        print("Scissors cut Paper, Computer wins")
    elif (computer_choice == "Scissors" and player_choice == "Rock"):
        print(f"Rock Smashes Scissors, {player_name} wins")
    elif (computer_choice == "Rock" and player_choice == "Scissors"):
        print("Rock smashes Scissors, Computer wins")
    elif computer_choice == player_choice:
        print("It's a draw")
    else:
        print("Rock, Paper, and Scissors are the only choices allowed.")
