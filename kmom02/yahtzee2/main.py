#!/usr/bin/env python3

"""
Main module for terminal game loop application yahtzee.
"""
from src.hand import Hand


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


def menu(value):
    """
    Menu function for game loop.
    """
    print(
f"""
What is your next move?
...................

r       roll the dice.
q       quit the game.

..................................................
Your current dice hand value: {value}
..................................................
"""
    )
    user_input = input("Players choice? [r/q]: ")
    user_input = user_input.lower()
    return str(user_input)


def ask_dice_indexes():
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



if __name__ == "__main__":
    game_on = welcome()

    print(
"""
Starting a new game of Yatzy...
Rolling dice...
"""
    )
    dice_hand = Hand()
    dice_hand.roll()
    # round += 1
    hand_values = dice_hand.__str__()
    game_on = menu(hand_values)

    while game_on == "r" != "q":
        if game_on == "r":
            dice_indexes = ask_dice_indexes()
            dice_hand.roll(dice_indexes)
            hand_values = dice_hand.__str__()
            game_on = menu(hand_values)
        # round += 1

print(
"""
..............................
Thank you for playing with us!
Exiting Yatzy...

"""
)
