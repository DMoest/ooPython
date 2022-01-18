#!/usr/bin/env python3

import random


class Die():
    """Die class, represents a dice."""


    # Static attributes
    MIN_ROLL_VALUE = 1
    MAX_ROLL_VALUE = 6


    def __init__(self, _value=0):
        """
        Constructor method for class instance
        """
        self.sides = self.MAX_ROLL_VALUE
        self._value = 0


    def __str__(self):
        """
        Return string representation for attribute _value
        """
        return str(self._value)


    def roll(self):
        """
        Setter method for dice value from roll action.
        Value is generated randomly from range defined with
        the static attributes MIN_ROLL_VALUE and MAX_ROLL_VALUE.
        """
        dice_value = random.randrange(self.MIN_ROLL_VALUE, self.MAX_ROLL_VALUE, 1)

        return dice_value


    def get_name(self):
        """
        Getter method to return string representation of the dice value.
        """
        value = self.get_value()

        if value == 1:
            return "one"
        elif value == 2:
            return "two"
        elif value == 3:
            return "three"
        elif value == 4:
            return "four"
        elif value == 5:
            return "five"
        elif value == 6:
            return "six"
        elif value == 0:
            return "No dice have been rolled yet... "


    def get_value(self):
        """
        Getter method to return the dice value.
        """
        return self._value


    def get_sides(self):
        """
        Getter method to return number of sides on dice.
        """
        return self.sides
