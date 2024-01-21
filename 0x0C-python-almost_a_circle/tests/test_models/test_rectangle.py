#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
import os
import sys
from models.base import Base
class TestRectangle(unittest.TestCase):
    def test_inheritance(self):
        rec = Rectangle(2,4)
        self.assertTrue(isinstance(rec, Rectangle))
        self.assertTrue(isinstance(rec, Base))

    def test_valid_integer(self):
        rec = Rectangle(10, 2, 3, 1)
        self.assertEqual(rec.width, 10)
        self.assertEqual(rec.height, 2)
        self.assertEqual(rec.x, 3) 
        self.assertEqual(rec.y, 1)

    def test_strings(self):
        with self.assertRaises(TypeError):
             Rectangle(10, "2")
        with self.assertRaises(TypeError):
            Rectangle("34",5)
    def test_negative_integer(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)
