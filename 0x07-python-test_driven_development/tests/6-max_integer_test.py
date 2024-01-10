#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_number(self):
        """This check for max_num along the real numbers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_number(self):
        """ This checks for max_num within the negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_real_and_negative(self):
        """ This checks the max_number betwwen positive and negative"""
        self.assertEqual(max_integer([-4, 1]), 1)

    def test_strings(self):
        """This test strings """
        with self.assertRaises(TypeError):
            max_integer([1, "string", 5])

    def test_float_number(self):
        """Check for flaot_numberds"""
        self.assertEqual(max_integer([3.4, 5.7]), 5.7)

    def test_empty_list(self):
        """ check empty list"""
        self.assertIsNone(max_integer([]), "Empty list return None")

    def test_one_item(self):
        """ check when the item is one in a list"""
        self.assertEqual(max_integer([1]), 1)

    def test_none(self):
        """ check for None """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_max_at_beginning(self):
        """ this check when the max number is at the beginning"""
        self.assertEqual(max_integer([100, 2, 4, 5]), 100)

    def test_max_middle(self):
        """check when the max is at the middle"""
        self.assertEqual(max_integer([1, 44, 5]), 44)
