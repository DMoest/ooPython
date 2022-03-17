#!/usr/bin/env python3

"""
All Rules module.
"""
from abc import ABC, abstractmethod


class Rule(ABC):
    """
    Rule abstract class.
    Represents a base rule for yatzy game rules to be implemented from.
    """

    @abstractmethod
    def points(self, hand):
        """
        Points method for class.
        """

class SameValueRule(Rule):
    """
    SameValueRule class.
    """

    def __init__(self, value, name):
        """
        Class instance constructor method.
        """
        self.value = value
        self.name = name

    def points(self, hand):
        """
        Getter method to compare and count equal dice values in hand to the rule value.
        """
        points = 0

        for dice in hand.get_dice():
            if dice.__eq__(self.value):
                points += self.value

        return points

class Ones(SameValueRule):
    """
    Ones class.
    """

    def __init__(self):
        """
        Class constructor method.
        """
        super().__init__(1, "Ones")


class Twos(SameValueRule):
    """
    Twos class.
    """

    def __init__(self):
        """
        Class constructor method.
        """
        super().__init__(2, "Twos")


class Threes(SameValueRule):
    """
    Threes class.
    """

    def __init__(self):
        """
        Class constructor method.
        """
        super().__init__(3, "Threes")


class Fours(SameValueRule):
    """
    Fours class.
    """

    def __init__(self):
        """
        Class constructor method.
        """
        super().__init__(4, "Fours")


class Fives(SameValueRule):
    """
    Fives class.
    """

    def __init__(self):
        """
        Class constructor method.
        """
        super().__init__(5, "Fives")


class Sixes(SameValueRule):
    """
    Sixes class.
    """

    def __init__(self):
        """
        Class constructor method.
        """
        super().__init__(6, "Sixes")


class ThreeOfAKind(Rule):
    """
    ThreeOfAKind class.
    """

    def __init__(self):
        """
        Class constructor method.
        """
        self.name = "Three Of A Kind"

    def points(self, hand):
        """
        Getter method for points in hand if three of a kind.
        """
        dice_values = hand.to_list()
        points = sum(hand.to_list())
        dice_values.sort()

        if dice_values[0] == dice_values[2] or \
                dice_values[1] == dice_values[3] or \
                dice_values[2] == dice_values[4]:
            return points

        return 0


class FourOfAKind(Rule):
    """
    FourOfAKind class.
    """

    def __init__(self):
        """
        Class constructor method.
        """
        self.name = "Four Of A Kind"

    def points(self, hand):
        """
        Getter method for points in hand if three of a kind.
        """
        dice_values = hand.to_list()
        points = sum(hand.to_list())
        dice_values.sort()
        condition_1 = dice_values[0] == dice_values[3]
        condition_2 = dice_values[1] == dice_values[4]

        if condition_1 or condition_2:
            return points
        return 0


class SmallStraight(Rule):
    """
    SmallStraight class.
    """

    def __init__(self):
        """
        Class constructor method.
        """
        self.name = "Small Straight"

    def points(self, hand):
        """
        Getter method for points in hand if three of a kind.
        """
        dice_values = hand.to_list()
        dice_values.sort()

        if all(x in dice_values for x in range(1, 5)) or \
                all(x in dice_values for x in range(2, 6)) or \
                all(x in dice_values for x in range(3, 7)) is True:
            return 30
        return 0


class LargeStraight(Rule):
    """
    LargeStraight class.
    """

    def __init__(self):
        """
        Class constructor method.
        """
        self.name = "Large Straight"

    def points(self, hand):
        """
        Getter method for points in hand if three of a kind.
        """
        dice_values = hand.to_list()
        dice_values.sort()

        if all(x in dice_values for x in range(1, 6)) or \
                all(x in dice_values for x in range(2, 7)):
            return 40
        return 0


class FullHouse(Rule):
    """
    FullHouse class.
    """

    def __init__(self):
        """
        Class constructor method.
        """
        self.name = "Full House"

    def points(self, hand):
        """
        Getter method for points in hand if three of a kind.
        """
        dice_values = hand.to_list()
        dice_values.sort()
        condition_1 = dice_values[0] == dice_values[1] and \
                      dice_values[2] == dice_values[4] and \
                      dice_values[0:1] != dice_values[2:3]
        condition_2 = dice_values[0] == dice_values[2] and \
                      dice_values[3] == dice_values[4] and \
                      dice_values[0:1] != dice_values[3:4]

        if condition_1 or condition_2:
            return 25

        return 0


class Chance(Rule):
    """
    Chance class.
    """

    def __init__(self):
        """
        Class constructor method.
        """
        self.name = "Chance"

    def points(self, hand):
        """
        Getter method for points in hand if three of a kind.
        """
        points = sum(hand.to_list())

        return points


class Yahtzee(Rule):
    """
    Yahtzee class.
    """

    def __init__(self):
        """
        Class constructor method.
        """
        self.name = "Yahtzee"

    def points(self, hand):
        """
        Getter method for points in hand if three of a kind.
        """
        dice_values = hand.to_list()
        # points = sum(dice_values)
        dice_values.sort()

        if dice_values[0] == dice_values[4]:
            return 50

        return 0
