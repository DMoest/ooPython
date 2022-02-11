#!/usr/bin/env python3

"""
Handler module.
"""
from flask import session
from src.hand import Hand

class Handler:
    """
    Handler class.
    """

    def __init__(self):
        """
        Constructor method for class.
        """
        self.hand = Hand()
        self.keepers = []
        self.scoreboard = {}

    def get_hand(self):
        """
        Getter method for hand.
        """
        return self.hand

    def roll(self, indexes=None):
        """
        Roll dice in hand. If indexes given only roll those dices.
        """
        if indexes:
            return self.hand.roll(indexes)
        return self.hand.roll()

    def add_to_scoreboard(self, request_form):
        """
        Setter method to keep dice values.
        """
        if session.get('scoreboard') is None:
            session['scoreboard'] = {}
            self.scoreboard = {}
        else:
            self.scoreboard = session.get('scoreboard')

        key = request_form['select_score']
        value = int(request_form[key])
        self.scoreboard[key] = value
        session['scoreboard'] = self.scoreboard

        return self.scoreboard
