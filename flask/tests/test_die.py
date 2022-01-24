#!/usr/bin/env python3

"""
Test module for instances of class Die.
"""
import unittest
import random
from src.die import Die


class TestDie(unittest.TestCase):
    """
    Submodule for unittests, derives from unittest.TestCase
    """

    def setUp(self):
        """
        Build up method that runs before each test case.
        """
        random.seed("oopython")
        self.die = Die()

    # def tearDown(self):
    #     """
    #     Tear down method that runs after each test case.
    #     """

    def test_initial_die_values(self):
        """
        Test the initial values on a new object instance of die.
        """
        self.assertEqual(self.die.get_value(), 4)
        self.assertNotEqual(self.die.get_value(), "")
        self.assertNotEqual(self.die.get_value(), [])
        self.assertNotEqual(self.die.get_value(), ())
        self.assertEqual(self.die.MIN_ROLL_VALUE, 1)
        self.assertEqual(self.die.MAX_ROLL_VALUE, 6)

        self.assertEqual(self.die.MIN_ROLL_VALUE, 1)
        # Ska man kunna välja antal sidor på en tärning blir det här fel...
        self.assertEqual(self.die.MAX_ROLL_VALUE, 6)

    def test_die_attribute_types(self):
        """
        Test types on object instance attributes.
        """
        self.assertEqual(type(self.die.get_value()), int)
        self.assertNotEqual(type(self.die.get_value()), str)
        self.assertNotEqual(type(self.die.get_value()), bool)
        self.assertNotEqual(type(self.die.get_value()), list)
        self.assertNotEqual(type(self.die.get_value()), dict)
        self.assertNotEqual(type(self.die.get_value()), tuple)

        self.assertEqual(type(self.die.__str__()), str)
        self.assertNotEqual(type(self.die.__str__()), int)
        self.assertNotEqual(type(self.die.__str__()), bool)
        self.assertNotEqual(type(self.die.__str__()), list)
        self.assertNotEqual(type(self.die.__str__()), dict)
        self.assertNotEqual(type(self.die.__str__()), tuple)

        self.assertEqual(type(self.die.get_name()), str)
        self.assertNotEqual(type(self.die.get_name()), int)
        self.assertNotEqual(type(self.die.get_name()), bool)
        self.assertNotEqual(type(self.die.get_name()), list)
        self.assertNotEqual(type(self.die.get_name()), dict)
        self.assertNotEqual(type(self.die.get_name()), tuple)

    def test_die_object_for_instance_of_class(self):
        """
        Test for the initial value
        """
        self.assertIsInstance(self.die, Die)

    def test_die_roll_value_type(self):
        """
        Test die roll value type
        """
        self.assertEqual(type(self.die.roll()), int)
        self.assertNotEqual(type(self.die.roll()), str)
        self.assertNotEqual(type(self.die.roll()), bool)
        self.assertNotEqual(type(self.die.roll()), list)
        self.assertNotEqual(type(self.die.roll()), dict)
        self.assertNotEqual(type(self.die.roll()), tuple)

    def test_random_dice_roll(self):
        """
        Test die roll for random value with random seed
        """
        self.assertEqual(self.die.roll(), 1)
