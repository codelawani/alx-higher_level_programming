#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init_with_positive_integers(self):
        print('R:test_init_with_positive_integers')
        r = Rectangle(4, 6, 3, 1, 12)
        self.assertEqual(r.width, 4)

    def test_init_negative_integers(self):
        print('R:test_init_negative_integers')
        self.assertRaises(ValueError, Rectangle, -4, 6)
        self.assertRaises(ValueError, Rectangle, 4, -6)
        self.assertRaises(ValueError, Rectangle, 4, 6, -2)
        self.assertRaises(ValueError, Rectangle, 4, 6, 2, -4)

    def test_init_with_string(self):
        print('test_init_with_string')
        with self.assertRaises(TypeError):
            Rectangle('a', 'b')

    def test_init_with_None(self):
        print('test_init_with_None')
        with self.assertRaises(TypeError):
            Rectangle(None, None)
