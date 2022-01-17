#!/usr/bin/env python3

import random

class Die():

    # Static attributes
    MIN_ROLL_VALUE = 1
    MAX_ROLL_VALUE = 6


    def __init__(self, _value=0, sides=6):
        """
        Constructor method for class objects
        """
        self.sides = sides
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
        match self._value:
            case 1:
                return "one"
            case 2:
                return "two"
            case 3:
                return "three"
            case 4:
                return "four"
            case 5:
                return "five"
            case 6:
                return "six"


    def get_value(self):
        """
        Getter method to return the dice value.
        """
        return self._value
