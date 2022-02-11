#!/usr/bin/env python3

"""
Handler module.
"""

import inspect
import sys


def welcome():
    """
    Welcome prompt for game loop yahtzee1 game.
    """
    print(
        """
        Welcome to a game of Yatzy!
        ...........................
        Created by: Daniel Andersson
        Version 1.0.0
        """
    )
    return "start game"


def ask_for_dice_index():
    """
    Function to ask player for dice indexes to play.
    """
    print(
        """
        Choose which dices you like to roll.
        Use index numbers in range 0 - 4 to select.
        You can separate indexes with a space to select several dice.
        If you do not select any, all of them will be rolled.
        """
    )
    indexes = [0, 1, 2, 3, 4]
    user_input = input("Choose dices to roll [0 1 2 3 4]: ")
    user_input = user_input.lower()
    message = "Rolling dice: "

    if len(user_input) > 0:
        indexes = [int(index) for index in user_input.split(" ")]
        for index in indexes:
            if 0 > index > 4:
                print("Opps... you have an unvalid input index. Try between 0 and 4.")
            else:
                message += str(index) + " "

        print(f"{message}")
        return list(indexes)

    print("Rolling all dice in hand... ")
    return indexes


class Handler:
    """
    Handler class
    """

    def __init__(self):
        """
        Constructor method for Handler class.
        """
        self._options = {
            "r": "ask_for_dice_index",
            "roll": "ask_for_dice_index",
            "q": "quit",
            "quit": "quit",
        }

    def main(self):
        """
        Entrypoint for program
        """
        while True:
            self._print_menu()
            c = input("Enter: ")
            try:
                self._get_method(c)()
            except KeyError:
                input("Invalid choice!\nPress any key to continue")

    def _print_menu(self):
        """
        Use docstring from methods to print options for the program
        https://docs.python.org/3/library/inspect.html#inspect.getdoc
        """
        menu = "-------------------------\n"
        # loop over all options in dictionary
        for key in sorted(self._options):
            # Use _get_method to dynamically get method
            method = self._get_method(key)
            # Use getdoc to get docstring from method
            docstring = inspect.getdoc(method)

            # format meny choice text
            menu += "{choice}: {explanation}\n".format(
                choice=key,
                explanation=docstring
            )

        print(menu, )

    def _get_method(self, method_name):
        """
        Use function getattr() to dynamically get value of an attribute.
        https://docs.python.org/3.7/library/functions.html#getattr
        If attribute is a method, a reference to the method is returned.
        For an example, https://www.journaldev.com/16146/python-getattr
        """
        return getattr(self, self._options[method_name])

    @staticmethod
    def quit():
        """
        Exit program
        """
        return sys.exit()


if __name__ == "__main__":
    handler = Handler()
    handler.main()
