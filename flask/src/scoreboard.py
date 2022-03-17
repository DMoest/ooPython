#!/usr/bin/env python3

"""
Scoreboard module.
"""
from flask import session


class Scoreboard:
    """
    Scoreboard Class.
    """

    def __init__(self, scores, the_rules):
        print(" ---> Scoreboard.__init__() ")
        # print(f" - Scoreboard.__init__({scores}, {the_rules}) ")
        self.points = 0
        self.rules = the_rules
        self.scores = scores

    def get_total_points(self):
        """
        Getter method for total points.
        """
        # print(" ---> Scoreboard.get_total_points() ")
        total_points = 0

        # print(f"self.scores {self.scores}")
        for score in self.scores:
            if self.scores[score] == -1:
                total_points += 0
            else:
                total_points += self.scores[score]
        return total_points

    def add_points(self, rule_name, hand):
        """
        Setter method to set points to scoreboard.
        """
        # print(f" ---> Scoreboard.add_points({rule_name}, {hand}) ")
        self.scores = session.get('scoreboard')
        self.scores[rule_name] = self.rules[rule_name].points(hand)

        return self.scores[rule_name]

    def get_points(self, rule_name):
        """
        Getter method to return points for rule name.
        """
        # print(f" ---> Scoreboard.get_points({rule_name}) ")
        return self.scores[rule_name]

    def get_scoreboard(self):
        """
        Getter method to return scoreboard dictionary.
        """
        # print(" ---> Scoreboard.get_scoreboard() ")
        return self.scores

    def finished(self):
        """
        Getter method to return boolean indicating if game is finished.
        """
        # print(" ---> Scoreboard.finished() ")
        self.scores = session.get('scoreboard')
        finished = True

        for score in self.scores:
            if self.scores[score] == -1:
                finished = False

        return finished

    @classmethod
    def from_dict(cls, list_of_rule_classes):
        """
        Getter method from dict.
        """
        print(" ---> Scoreboard.from_dict()")
        # print(f" - Scoreboard.from_dict({list_of_rule_classes})")
        scores = {}
        rules = {}

        for rule in list_of_rule_classes:
            rules[rule.name] = rule
            scores[rule.name] = -1

        new_scoreboard = Scoreboard(scores, rules)

        return new_scoreboard
