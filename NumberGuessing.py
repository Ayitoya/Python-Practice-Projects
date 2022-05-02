import random
attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score, It's yours for the taking!")
    else:
        print("The current high score is {} attempts" .format(min(attempts_list)))
def start_game():
    random_number = int(random.randint(1,10))
    print("Hello traveler! Welcome to the game of guesses!")
    player_name = input("What's your name? ")
    wanna_play = input("Hi, {}, would you like to play the guessing game? (Enter yes/no) ".format(player_name))
    # Where the show_score function used to be
    attempts = 0
    show_score()
    while wanna_play == "yes":
        try:
            guess = input("Pick a number between 1 and 10 ")
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Please guess a number within the given range")
            if int(guess) == random:
                print("NIce! You got it!")
                attempts += 1
                attempts_list.append(attempts)
                print("It took you {} attempts".format(attempts))
                play_again = input("Would you like to play again? (Enter Yes/No) ")
                attempts = 0
                show_score()
                random_number = int(random.randint(1,10))
                if play_again.lower() == "no":
                    print("That's cool, Have a good one!")
                    break
            elif int(guess) > random_number:
                print("It's lower")
                attempts += 1
            elif int(guess) < random_number:
                print("It's higher")
                attempts += 1
        except ValueError as err:
            print("Oh no!, that is not a valid value. Try again...")
            print("({})".format(err))
    else:
        print("That's cool, have a good one!")
if __name__ == '_main_':
    start_game()