#!/usr/bin/env python3

"""
Hand class module.
"""
from src.die import Die


class Hand:
    """
    Hand class, represents a hand of dices.
    """

    def __init__(self, dice=None, num_of_dice=5):
        """
        Constructor method for class instance.
        """
        self.dice = []

        if dice is not None:
            for value in dice:
                self.dice.append(Die(value))
        else:
            x = 0
            while x < num_of_dice:
                self.dice.append(Die())
                x += 1

    def __str__(self):
        """
        Getter method to return string of values from dice in hand
        """
        output_string = ""
        for index, dice in enumerate(self.dice):
            output_string += str(dice.get_value())
            if index < len(self.dice) - 1:
                output_string += ", "

        return output_string

    def roll(self, indexes=None):
        """
        Setter method to roll dices in hand
        """
        hand_values = []

        for index, dice in enumerate(self.dice):
            if indexes is None or index in indexes:
                dice.roll()
                hand_values.append(dice.get_value())
            elif indexes is not None and index not in indexes:
                hand_values.append(dice.get_value())

        return hand_values

    def to_list(self):
        """
        Getter method for list of values of dice in hand.
        """
        values = []
        for dice in self.dice:
            values.append(dice.get_value())

        return values

    def get_total_value(self):
        """
        Getter method to calculate and return the total value of dices in hand.
        """
        total = 0
        for dice in self.dice:
            total += dice.get_value()

        return total

    def get_dice(self):
        """
        Getter method for returning dice objects in hand.
        """
        return self.dice
