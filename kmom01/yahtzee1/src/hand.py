#!/usr/bin/env python3

"""
Hand class module.
"""
from src.die import Die


class Hand():
    """
    Hand class, represents a hand of dices.
    """

    def __init__(self, dice=None):
        """
        Constructor method for class instance
        """
        self.indexes = []
        self.dice = []
        self._values = []
        x = 0

        if dice is not None and dice > 0:
            while x < 5:
                self.dice.append(Die(dice[x]))
                self.indexes.append(x)
                self._values.append(self.dice[x].get_value())
                x += 1

        else:
            while x < 5:
                self.dice.append(Die())
                self.indexes.append(x)
                self._values.append(self.dice[x].get_value())
                x += 1

    def __str__(self):
        """
        Getter method to return string of values from dice in hand
        """
        output_string = ""
        x = 0

        while x < len(self._values):
            value = self.dice[x].get_value()
            output_string += str(value)

            if x != len(self._values) - 1:
                output_string += ","

            x += 1

        return output_string

    def roll(self, indexes=None):
        """
        Setter method to roll dices in hand
        """
        if indexes is None:
            for dice_index in self.indexes:
                value = self.dice[dice_index].roll()
                self._values[dice_index] = value
        elif len(indexes) > 0:
            for dice_index in indexes:
                if 0 <= dice_index <= 4:
                    value = self.dice[dice_index].roll()
                    self._values[dice_index] = value
                else:
                    print("Opps... somethings wrong with your input indexes. ")

        return self._values

    def get_values(self):
        """
        Getter method for list of values of dice in hand.
        """
        return self._values

    def get_total_value(self):
        """
        Getter method to calculate and return the total value of dices in hand.
        """
        total = 0

        for value in self.get_values():
            total += value

        return total

    def get_dice(self):
        """
        Getter method for returning dice objects in hand.
        """
        return self.dice
