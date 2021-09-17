#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Sept 2021
# This program is the number guessing game

import constants


def main():
    guess_number = int(input("Enter a number as your guess (1-9): "))

    if guess_number == constants.ANSWER:
        print("You guessed correctly!")
    else:
        print("You guessed incorrectly.")
    print("The correct answer is {0}.".format(constants.ANSWER))
    print("\nDone.")


if __name__ == "__main__":
    main()
