# Kibo FPWP Final Project
# Put your final project code in this file for submission
# Add the names of the authors, a brief description, and link to your video in the file called 'readme.md'
# Then, you can remove these instruction comments
from madlibs import madlibs_game
from quiz import quiz_func
from joke import bot_joke
#import random
print("Hi there I'm....")
while True:
  bot_choice = input("Sorry about that, I don't have a name could you please give me one? Type Y/N ")
  print()
  if bot_choice in ["Y", "y"]:
    bot_name = input("Enter the name: ")
    print()
    break
  elif bot_choice in ["N", "n"]:
    bot_name = "Bot"
    break
  else:
    print("Invalid input, Please enter Y/N")
    print()


print(f"My name is {bot_name}. How can I help you today?")
options = ["I want to play Madlibs", "I want to play the Quiz", "Tell me a programming joke", "Exit"]

while True:
  input("Press [enter] to continue.")
  for (i, option) in enumerate(options):
      print(f"{i + 1}. {option}")
  choice = input("Choose a number: ")
  if choice.isdecimal() == 1:
    madlibs_game()
  elif choice.isdecimal() == 2:
    quiz_func()
  elif choice.isdecimal() == 3:
    bot_joke()
  elif choice.isdecimal() == 4:
    print(f"Thanks for using {bot_name}")
    break
  else:
    print("You have to enter a number.")
  print()
  

  

  
  


