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
        self.die = []
        self._values = []

        if dice is None:
            x = 0

            while x < 5:
                self.die.append(Die())
                self.indexes.append(x)
                self._values.append(0)
                x += 1

        else:
            for die in dice:
                self.die.append(Die())
                self.indexes.append(die)
                if self.die[die].get_value() is None:
                    self._values.append(0)
                else:
                    self._values.append(self.die[die].get_value())


    def __str__(self):
        """
        Getter method to return string of values from dice in hand
        """
        output_string = ""
        x = 0

        while x < len(self._values):
            value = self.die[x].get_value()

            if value is None:
                output_string += str(0)
            else:
                output_string += str(value)

            if x != len(self._values) -1:
                output_string += ","

            x += 1

        return output_string


    def roll(self, indexes=None):
        """
        Setter method to roll dices in hand
        """
        if indexes is None:
            for die_index in self.indexes:
                value = self.die[die_index].roll()
                self._values[die_index] = value
        elif len(indexes) > 0:
            for die_index in indexes:
                if 0 <= die_index <= 4:
                    value = self.die[die_index].roll()
                    self._values[die_index] = value
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

        for value in self._values:
            if value == type(None):
                total += 0
            elif value == type(int):
                total += value

        return total
