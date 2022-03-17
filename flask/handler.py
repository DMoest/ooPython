#!/usr/bin/env python3

"""
Handler module.
"""
from flask import session
from src.hand import Hand
from src.scoreboard import Scoreboard
from src.rules import (
    Ones,
    Twos,
    Threes,
    Fours,
    Fives,
    Sixes,
    ThreeOfAKind,
    FourOfAKind,
    SmallStraight,
    LargeStraight,
    FullHouse,
    Chance,
    Yahtzee
)


class Handler:
    """
    Handler class.
    """
    RULES = [
        Ones(),
        Twos(),
        Threes(),
        Fours(),
        Fives(),
        Sixes(),
        ThreeOfAKind(),
        FourOfAKind(),
        SmallStraight(),
        LargeStraight(),
        FullHouse(),
        Chance(),
        Yahtzee()
    ]

    def __init__(self):
        """
        Constructor method for class.
        """
        print(" - Handler.__init__()")
        self.hand = Hand()
        self.scoreboard = Scoreboard.from_dict(self.RULES)
        self.scores = self.scoreboard.get_scoreboard()
        self.counter = 1
        self.dice_hand = []
        self.total_points = 0

    def get_hand(self):
        """
        Getter method for hand.
        """
        # print(" ---> Handler.get_hand()")
        if session.get('hand'):
            self.hand = self.read_session('hand')

        return self.hand

    def get_rules(self):
        """
        Getter method to return all rules for scoring.
        """
        # print(" ---> Handler.get_rules()")
        return self.RULES

    def get_counter(self):
        """
        Getter method to return counter.
        """
        # print(" ---> Handler.get_counter()")
        self.counter = self.read_session('counter')
        # if self.counter is None:
        #     self.counter = 0
        #     self.write_session('counter', self.counter)

        return self.counter

    def set_next_count(self):
        """
        Setter method to set nex counter.
        """
        # print(" ---> Handler.set_next_count()")
        self.counter = self.read_session('counter')

        if self.counter < 3:
            self.counter += 1
            self.write_session('counter', self.counter)
        elif self.counter >= 3:
            self.counter = 0
            self.write_session('counter', self.counter)

        return self.counter

    def roll(self, indexes=None):
        """
        Roll dice in hand. If indexes given only roll those dices.
        """
        # print(f" ---> Handler.roll(indexes={indexes})")
        self.dice_hand = self.read_session('dice_hand')

        if self.get_counter() < 3:
            self.dice_hand = self.hand.roll(self.read_session('roll_these_dice'))
            self.write_session('dice_hand', self.dice_hand)
            self.set_next_count()

    def get_dice_hand(self):
        """
        Getter method to return dice hand.
        """
        # print(" ---> Handler.get_dice_hand()")
        self.dice_hand = self.read_session('dice_hand')

        return self.dice_hand

    def get_scoreboard(self):
        """
        Getter method to get scoreboard.
        """
        # print(" ---> Handler.get_scoreboard()")
        self.scores = self.read_session('scoreboard')

        return self.scores

    def add_to_scoreboard(self, request_form):
        """
        Setter method to keep dice values.
        """
        # print(f" ---> Handler.add_to_scoreboard({request_form})")
        rule_name = request_form['select_score']

        # TODO make sure it writes to session correctly?
        self.scoreboard.add_points(rule_name, self.hand)
        new_scoreboard = self.read_session('scoreboard')

        self.write_session('scoreboard', new_scoreboard)
        self.write_session('counter', 0)

        return self.read_session('scoreboard')

    def get_total_score(self):
        """
        Getter method for total score on scoreboard.
        """
        # print(" ---> Handler.get_total_score() ")

        self.total_points = self.scoreboard.get_total_points()
        self.write_session('total_points', self.total_points)

        return self.total_points

    @staticmethod
    def check_sessions():
        """
        Static method to check if all sessions exist.
        """
        # print(" ---> Handler.check_sessions() ")
        check_ok = True

        if session.get('dice_hand') is None or \
                session.get('scoreboard') is None or \
                session.get('total_points') is None or \
                session.get('counter') is None or \
                session.get('finished') is None:
            check_ok = False

        return check_ok

    @staticmethod
    def setup_sessions(handler):
        """
        Setter method to setup all sessions for a game of yahtzee.

        1. Get all values to check.
        2. Write values to sessions.
        3. Return all session values.
        """
        # print(" ---> Handler.setup_sessions() ")

        # Aquire data
        rules = handler.get_rules()
        scoreboard = Scoreboard.from_dict(rules)
        new_scores = scoreboard.get_scoreboard()
        total_points = handler.get_total_score()

        # Write to session
        handler.write_session('scoreboard', new_scores)
        handler.write_session('total_points', total_points)
        handler.write_session('counter', 1)
        handler.write_session('finished', False)

    @staticmethod
    def write_session(session_name, assign_value):
        """
        Static method to write to session.
        """
        print(f" ---> Handler.write_session({session_name}) ")
        session[session_name] = assign_value

    @staticmethod
    def read_session(session_name):
        """
        Static method to read from session.
        """
        print(f" ---> Handler.read_session({session_name}) ")
        return session.get(session_name)

    def is_finished(self):
        """
        Getter method for finished game.
        """
        # print(" ---> Handler.is_finished() ")
        self.write_session('finished', self.scoreboard.finished())

        return self.scoreboard.finished()

    def reset_game(self):
        """
        Setter method to reset scoreboard.
        """
        # print(" ---> Handler.reset_game() ")
        session.clear()
        self.hand = Hand()
        self.scoreboard = Scoreboard.from_dict(self.RULES)
        self.counter = 0
