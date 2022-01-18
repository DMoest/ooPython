#!/usr/bin/env python3

"""
Test module for instances of class Hand.
"""
import unittest
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
        self.hand = Hand()


    # def tearDown(self):
    #     """
    #     Tear down method that runs after each test case.
    #     """


    def test_initial_hand_values(self):
        """
        Test the initial values on a new object instance of die.
        """
        self.assertEqual(self.hand.get_total_value(), 0)
        self.assertEqual(self.hand.__str__(), "0,0,0,0,0")


    def test_hand_attribute_types(self):
        """
        Test types on object instance attributes.
        """
        self.assertEqual(type(self.hand.get_total_value()), int)
        self.assertNotEqual(type(self.hand.get_total_value()), str)
        self.assertNotEqual(type(self.hand.get_total_value()), bool)
        self.assertNotEqual(type(self.hand.get_total_value()), list)
        self.assertNotEqual(type(self.hand.get_total_value()), dict)
        self.assertNotEqual(type(self.hand.get_total_value()), tuple)

        self.assertEqual(type(self.hand.__str__()), str)
        self.assertNotEqual(type(self.hand.__str__()), int)
        self.assertNotEqual(type(self.hand.__str__()), bool)
        self.assertNotEqual(type(self.hand.__str__()), list)
        self.assertNotEqual(type(self.hand.__str__()), dict)
        self.assertNotEqual(type(self.hand.__str__()), tuple)

        self.assertEqual(type(self.hand.indexes), list)
        self.assertNotEqual(type(self.hand.indexes), str)
        self.assertNotEqual(type(self.hand.indexes), bool)
        self.assertNotEqual(type(self.hand.indexes), int)
        self.assertNotEqual(type(self.hand.indexes), dict)
        self.assertNotEqual(type(self.hand.indexes), tuple)

        self.assertEqual(type(self.hand.die), list)
        self.assertNotEqual(type(self.hand.die), str)
        self.assertNotEqual(type(self.hand.die), bool)
        self.assertNotEqual(type(self.hand.die), int)
        self.assertNotEqual(type(self.hand.die), dict)
        self.assertNotEqual(type(self.hand.die), tuple)

        self.assertEqual(type(self.hand.values), list)
        self.assertNotEqual(type(self.hand.values), str)
        self.assertNotEqual(type(self.hand.values), bool)
        self.assertNotEqual(type(self.hand.values), int)
        self.assertNotEqual(type(self.hand.values), dict)
        self.assertNotEqual(type(self.hand.values), tuple)


    def test_hand_object_for_instance_of_class(self):
        """
        Test hand for object instances.
        """
        self.assertIsInstance(self.hand, Hand)
        self.assertNotIsInstance(self.hand, Die)


    def test_die_objects_in_hand_for_instance_of_class(self):
        """
        Test dice hand dices for object instances.
        """
        for die in self.hand.die:
            self.assertIsInstance(die, Die)
            self.assertNotIsInstance(die, Hand)


    def test_hand_roll_value_type(self):
        """
        Test die roll value type
        """
        self.assertEqual(type(self.hand.roll()), list)
        self.assertNotEqual(type(self.hand.roll()), str)
        self.assertNotEqual(type(self.hand.roll()), int)
