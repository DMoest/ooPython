#!/usr/bin/env python3

# Module imports
import unittest
from src.die import Die


class TestDie(unittest.TestCase):
    """
    Submodule for unittests, derives from unittest.TestCase
    """

    def setUp(self):
        """
        Build up method that runs before each test case.
        """
        self.die = Die()


    # def tearDown(self):
    #     """
    #     Tear down method that runs after each test case.
    #     """


    def test_initial_die_values(self):
        """
        Test the initial values on a new object instance of die.
        """
        self.assertEqual(self.die.get_value(), 0)
        self.assertEqual(self.die.sides, 6)
        self.assertEqual(self.die.MIN_ROLL_VALUE, 1)
        self.assertEqual(self.die.MAX_ROLL_VALUE, 6)


    def test_die_attribute_types(self):
        """
        Test types on object instance attributes.
        """
        self.assertEqual(type(self.die.get_value()), int)
        self.assertEqual(type(self.die.sides), int)
        self.assertEqual(type(self.die.__str__()), str)
        self.assertEqual(type(self.die.get_name()), str)


    def test_die_object_for_instance_of_class(self):
        """
        Test for the initial value
        """
        self.assertIsInstance(self.die, Die)


    def test_die_roll_value(self):
        """
        Test die roll value type
        """
        self.assertEqual(type(self.die.roll()), int)
