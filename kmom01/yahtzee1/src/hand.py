#!/usr/bin/env python3

from die import Die


class Hand():
    """Hand class, represents a hand of dices. """

    def __init__(self, numOfDices=5):
        """
        Constructor method for class instance
        """
        self.indexes = []
        self.dice = []
        self.values = [0,0,0,0,0]
        x = 0

        while x <= numOfDices:
            self.dice.append(Die())
            self.indexes.append(x)
            x += 1


    def __str__(self):
        """Getter method to return string of values from dices in hand"""
        stringValues = [str(value) for value in self.values]
        outputString = ",".join(stringValues)

        return outputString


    def roll(self, indexes=[0,1,2,3,4]):
        """Setter method to roll dices in hand"""
        print(f"Incoming dice indexes {indexes} ")

        for diceIndex in indexes:
            value = self.dice[diceIndex].roll()
            self.values[diceIndex] = value


    def total_value(self):
        """Getter method to calculate and return the total value of dices in hand."""
        total = 0

        for value in self.values:
            total += value

        return total
