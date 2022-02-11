#!/usr/bin/env python3

"""
Test module for instances of class Hand.
"""
import unittest
import random
from src.hand import Hand
from src.die import Die


class TestHand(unittest.TestCase):
    """
    Submodule for unittests, derives from unittest.TestCase
    """

    def setUp(self):
        """
        Build up method that runs before each test case.
        """
        random.seed("oopython")
        self.hand = Hand([2, 3, 1, 4, 6])

    def tearDown(self):
        """
        Tear down method that runs after each test case.
        """
        del self.hand

    def test_hand_class_methods_values(self):
        """
        Test the initial values on a new object instance of die.
        """
        self.assertEqual(self.hand.get_total_value(), 16)
        self.assertEqual(self.hand.__str__(), "2, 3, 1, 4, 6")
        self.assertEqual(self.hand.to_list(), [2, 3, 1, 4, 6])  # Initial value
        self.assertEqual(self.hand.roll(), [4, 6, 1, 2, 3])  # New roll value

    def test_hand_attribute_types(self):
        """
        Test types on object instance attributes.
        """
        self.assertEqual(type(self.hand.get_total_value()), int)
        self.assertEqual(type(self.hand.__str__()), str)
        self.assertEqual(type(self.hand.dice), list)
        self.assertEqual(type(self.hand.to_list()), list)

    def test_hand_object_for_instance_of_class(self):
        """
        Test hand for object instances.
        """
        self.assertIsInstance(self.hand, Hand)

    def test_die_objects_in_hand_for_instance_of_class(self):
        """
        Test dice hand dices for object instances.
        """
        for die in self.hand.dice:
            self.assertIsInstance(die, Die)

    def test_hand_roll_value_type(self):
        """
        Test hand roll value type
        """
        self.assertEqual(type(self.hand.roll()), list)

    def test_hand_to_list_type(self):
        """
        Test hand roll value type
        """
        self.assertEqual(type(self.hand.to_list()), list)

    def test_hand_roll_dice_from_list_of_index(self):
        """
        Test hand roll form list of index for dice to roll.
        """
        list_of_index = [0, 3, 4]
        self.hand.roll(list_of_index)
        self.assertEqual(self.hand.to_list(), [4, 3, 1, 6, 1])

    def test_hand_roll_all_dice(self):
        """
        Test hand roll form list of index for dice to roll.
        """
        self.hand.roll()
        self.assertNotEqual(self.hand.to_list(), [2, 3, 1, 4, 6])
        self.assertEqual(self.hand.to_list(), [4, 6, 1, 2, 3])
