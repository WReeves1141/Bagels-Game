"""
pico - guess has a correct digit in the wrong place
fermi - guess has a correct digit in wrong place
bagels - no correct digits
10 tries

This program plays the Bagels game.
"""
import random

MAX_GUESSES = 10


def get_user_guess():
    """Gets a whole number input from the user."""
    return int(input("Enter your guess between 1 and 999 > "))


is_game_on = True
rand_number = str(random.randint(0, 999))
user_guess = 1
l_user_guess = []
print(rand_number)     # Temp

# Displays instructions.
print("Welcome to the bagel game!")
print("If 'Pico' is displayed, you have a correct digit in the wrong place.")
print("If 'Fermi' is displayed, " \
      "you have a correct digit in the correct place.")
print("If 'Bagels' is displayed, you have no correct digits.\n")

while is_game_on:
    printed_line = False

    while 999 >= user_guess >= 1:
        try:
            get_user_guess()
        except ValueError:
            print("Please enter a whole number.")
            get_user_guess()

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

    print(l_user_guess)     # Temp

    play_again = input("Would you like to play again? (y/n) > ")
    play_again = play_again.lower()

    if play_again == 'n':
        is_game_on = False
    elif play_again != 'y':
        print("Invalid Input.")
