#!/usr/bin/env python3

"""
Coin flip exersice from lecture.
"""

import random

class Coin():
    """
    Coin class.
    """

    def __init__(self):
        """
        Constructor method.
        """
        self.side_up = "Heads"
        self.results = []


    def toss_coin(self):
        """
        Setter method to toss coin.
        """
        possible_outcome = ["Heads", "Tails"]
        self.side_up = random.choice(possible_outcome)
        # self.results.append(self.side_up)

        return self.side_up




if __name__ == "__main__":
    # Init object & play variable.
    coin1 = Coin()
    play_again = "yes"

    while play_again == "yes" != "no":
        # Play coin toss with new object
        result = coin1.toss_coin()

        # Print result
        print("You tossed: " + result + ". ")

        # Prompt to play again
        print("Would you like to toss the coin again? [yes/no]")
        play_again = input()
