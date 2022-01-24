#!/usr/bin/env python3

"""
Die class module.
"""
import random


class Die():
    """Die class, represents a dice."""

    # Static attributes
    MIN_ROLL_VALUE = 1
    MAX_ROLL_VALUE = 6


    def __init__(self, value=None):
        """
        Constructor method for class instance
        """
        self._value = value


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
        self._value = random.randrange(self.MIN_ROLL_VALUE, self.MAX_ROLL_VALUE, 1)

        return self._value


    def get_name(self):
        """
        Getter method to return string representation of the dice value.
        """
        value = self.get_value()

        if value == 1:
            output_string = "one"
        elif value == 2:
            output_string = "two"
        elif value == 3:
            output_string = "three"
        elif value == 4:
            output_string = "four"
        elif value == 5:
            output_string = "five"
        elif value == 6:
            output_string = "six"
        else:
            output_string = "No dice have been rolled yet... "

        return output_string


    def get_value(self):
        """
        Getter method to return the dice value.
        """
        return self._value
