# ========================================================================== #
# Programmer : Walter Reeves
#
# Description:
#   This program plays a game of Bagels.
# ========================================================================== #
import random


def get_user_guess():
    """Gets a whole number input from the user."""
    return int(input("Enter your guess between 1 and 999 > "))


is_game_on = True
l_user_guess = []

# Displays instructions.
print("Welcome to the bagel game!")
print("If 'Pico' is displayed, you have a correct digit in the wrong place.")
print("If 'Fermi' is displayed, " \
      "you have a correct digit in the correct place.")
print("If 'Bagels' is displayed, you have no correct digits.")

while is_game_on:
    lives = 10
    user_guess = -1
    rand_number = str(random.randint(0, 999))
    while user_guess != rand_number:
        print(f"You have {lives} lives left.\n")
        printed_line = False
        user_guess = get_user_guess()
        while not isinstance(user_guess, int):
            print("Please enter a whole number.")
            user_guess = get_user_guess()
            try:
                user_guess = int(user_guess)
            except TypeError:
                print("test")

        user_guess = str(user_guess)
        for number in user_guess:
            l_user_guess.append(number)

        for xPosition in range(0, len(rand_number)):
            if user_guess[xPosition] in rand_number[xPosition]:
                print("Fermi", end=" ")
                printed_line = True
            elif user_guess[xPosition] in rand_number:
                print("Pico", end=" ")
                printed_line = True

        if not printed_line:
            print("Bagels")
        print()

    if user_guess != rand_number:
        lives -= 1
    elif lives == 0:
        print("You ran out of lives.\nGame Over")
    else:
        print("Congratulations you won!")

    play_again = input("Would you like to play again? (y/n) > ")
    play_again = play_again.lower()

    if play_again == 'n':
        is_game_on = False
        print("Thank you for playing!")
    elif play_again != 'y':
        print("Invalid Input.")
