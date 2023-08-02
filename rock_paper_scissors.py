import random
from time import sleep

def rps(bot_name, player_name):
    # Welcome the user to the game
    print("Welcome to rock, paper, scissors. Good luck!")

    # Initialize scores
    bot_score, player_score = 0, 0

    # Ask user for rounds
    while True:
        rounds = input("Enter the number of rounds you want to play: ")
        if not rounds.isdecimal():
            print("Enter valid number of rounds")
            

        elif int(rounds) % 2 == 0:
            print("Rounds must be an odd number (1,3,5,...)")

        else:
            break

    # Play the game for the total number of rounds
    for round in range(int(rounds)):
        print(f"Round #{round + 1}")

        # Make a choice for the computer player
        computer_choice = random.choice(["r", "p", "s"])

        # Get a choice from the user
        player_choice = input("Rock (r), Paper (p) or Scissors (s)? ")

        # Printing what the computer chooses
        print(f"The computer chooses {computer_choice}")

        # Compare the user and computer choice
        # Print the right message, based on the choices
        if (computer_choice == "r" and player_choice == "p"):
            print(f"Paper covers Rock, {player_name} wins this round")
            player_score += 1

        elif (computer_choice == "p" and player_choice == "r"):
            print(f"Paper covers Rock, {bot_name} wins this round")
            bot_score += 1

        elif (computer_choice == "p" and player_choice == "s"):
            print(f"Scissors cut Paper, {player_name} wins this round")
            player_score += 1

        elif (computer_choice == "s" and player_choice == "p"):
            print(f"Scissors cut Paper, {bot_name} wins this round")
            bot_score += 1

        elif (computer_choice == "s" and player_choice == "r"):
            print(f"Rock Smashes Scissors, {player_name} wins this round")
            player_score += 1

        elif (computer_choice == "r" and player_choice == "s"):
            print(f"Rock smashes Scissors, {bot_name} wins this round")
            bot_score += 1

        elif computer_choice == player_choice:
            print("It's a draw")

    sleep(2)

    print(f"{player_name} won {player_score} round(s)")
    print(f"{bot_name} won {bot_score} round(s)")

    if player_score > bot_score:
        print(f"{player_name} wins !!!")
    elif bot_score > player_score:
        print(f"{bot_name} wins !!!")
    else:
        print("It's a draw !!!")
        sleep(2)
        play_again = input("Do you want to play again? Y/N")
        if play_again.lower() == "y":
            rps()       
