#!/usr/bin/env python3

from src.hand import Hand


if __name__ == "__main__":
    game_on = "r"
    round = 1

    print("Rolling dice hand... ")

    dice_hand = Hand()
    dice_hand.roll()

    print(f"The result of your roll: {dice_hand.__str__()}")

    while game_on == "r" != "q" and round < 3:
        print("Do you want to roll the dices again? [yes/no]")
        game_on = input()

        if game_on == "r":
            print("Which dices would you like to roll again? [index of dices] ")
            dices = input()
            indexes = [int(num) for num in dices.split(" ")]

            print("Rolling dice hand... ")
            dice_hand.roll(indexes)

            print(f"The result of your last dice hand roll: {dice_hand.__str__()}")

        round += 1

print("Exit the game of Yatzy... ")
