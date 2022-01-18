#!/usr/bin/env python3

"""
Main test program.
"""
import unittest

if __name__ == '__main__':
    test_suit = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=3).run(test_suit)
