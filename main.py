# Kibo FPWP Final Project

from madlibs import madlibs_game
from quiz import quiz_func
from joke import bot_joke
from rock_paper_scissors import rps
from guess_my_number import guess_the_number
from time import sleep
from animate import animate



print("Hi there I'm....")
sleep(1.3)
while True:
    animate(
        "Sorry about that, I don't have a name could you please give me one? Type Y/N "
    )
    bot_choice = input()
    print()
    if bot_choice.lower() in ["y", "yes"]:
        bot_name = input("Enter the name: ")
        print()
        break
    elif bot_choice.lower() in ["n", "no"]:
        bot_name = "Bot"
        break
    else:
        print("Invalid input, Please enter Y/N")
        print()
player_name = input(f"My name is {bot_name}, What is your name: ")

if not player_name:
    player_name = "Player 1"
print(f"Nice to meet you {player_name}")

options = [
    "I want to play Madlibs",
    "I want to play the Quiz",
    "Tell me a programming joke",
    "Play Rock, Paper, Scissors",
    "Guess my Number",
    "Exit",
]

while True:
    input("Press [enter] to continue.")
    for (i, option) in enumerate(options):
        print(f"{i + 1}. {option}")
    choice = input("Choose a number: ")
    if choice.isdecimal() and int(choice) == 1:
        madlibs_game(bot_name, player_name)

    elif choice.isdecimal() and int(choice) == 2:
        quiz_func(player_name)

    elif choice.isdecimal() and int(choice) == 3:
        bot_joke()

    elif choice.isdecimal() and int(choice) == 4:
        rps(bot_name, player_name)

    elif choice.isdecimal() and int(choice) == 5:
        guess_the_number(bot_name, player_name)

    elif choice.isdecimal() and int(choice) == 6:
        print(f"Thanks for using {bot_name} the PlayBot")
        break
    else:
        print("You have to enter a number.")
    print()
