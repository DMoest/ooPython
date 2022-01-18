#!/usr/bin/env python3

"""
Hand class module.
"""
from src.die import Die


class Hand():
    """Hand class, represents a hand of dices. """

    def __init__(self, num_of_dices=5):
        """
        Constructor method for class instance
        """
        self.indexes = []
        self.die = []
        self.values = []
        x = 0

        while x < num_of_dices:
            self.die.append(Die())
            self.indexes.append(x)
            self.values.append(self.die[x].get_value())
            x += 1


    def __str__(self):
        """Getter method to return string of values from dices in hand"""
        string_values = [str(value) for value in self.values]
        output_string = ",".join(string_values)

        return output_string


    def roll(self, indexes=[]):
        """Setter method to roll dices in hand"""

        if len(indexes) == 0:
            try:
                for die_index in self.indexes:
                    value = self.die[die_index].roll()
                    self.values[die_index] = value
            except ValueError:
                print(f"Opps... somethings worng with your input indexes. \n {ValueError}")
        elif len(indexes) > 0:
            try:
                for die_index in indexes:
                    value = self.die[die_index].roll()
                    self.values[die_index] = value
            except ValueError:
                print(f"Opps... somethings worng with your input indexes. \n {ValueError}")

        return self.values


    def get_total_value(self):
        """Getter method to calculate and return the total value of dices in hand."""
        total = 0

        for value in self.values:
            total += value

        return total
