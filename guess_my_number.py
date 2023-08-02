def guess_the_number():
    import random
    print("I'm thinking of a number between 1 and 10\n")
    ran_num = random.randrange(10)
    print("To leave the game type cancel\n")
    print("To restart the game type restart\n")
# Ask the user to guess
# Check to see if the guess is <, >, or = secret number
    while ran_num < 10:
        user_num = input("Guess a number between 1 and 10: ")
        if user_num in ["exit", "Exit"]:
            break
        elif user_num in ["Restart", "restart"]:
            guess_the_number()
        elif user_num.isdecimal() == False:
            print("This is not a number")
        else:
            if int(user_num) == ran_num:
                print(f"Congratulations! The number was {user_num}\n")
                break
            elif int(user_num) < 5:
                print("Your guess is too low\n")
            elif int(user_num) >= 5 and int(user_num) <= 10:
                print("Your guess is too high\n")
            else:
                print("This number is not within range\n")