import random, time


def guess_the_number(bot_name, player_name):
    ran_num = random.randint(1, 10)
    print("I'm thinking of a number between 1 and 10\n")
    time.sleep(2)
    print("To leave the game type exit")
    print("To restart the game type restart")
    time.sleep(2)
    attempts = 3
    # Ask the user to guess
    # Check to see if the guess is <, >, or = secret number
    while True:
        if attempts == 0:
            print("You've run out of attempts.")
            break
        print(f"You have { attempts } attempts left.")
        user_inp = input(f"{player_name}, can you guess a number between 1 and 10: ")


        if user_inp.lower() == "exit":
            break
        elif user_inp in ["Restart", "restart"]:
            guess_the_number(bot_name, player_name)
            break
        elif user_inp.isdecimal() == False:
            print("This is not a number")
            continue
        
        # Check number in range
        user_num = int(user_inp)
        if user_num == ran_num:
            print(f"Congratulations! The number was {user_num}\n")
            break
        elif user_num < ran_num:
            print("Your guess is too low\n")

        elif user_num > ran_num:
            print("Your guess is too high\n")
        else:
            print("This number is not within range\n")

        attempts -= 1