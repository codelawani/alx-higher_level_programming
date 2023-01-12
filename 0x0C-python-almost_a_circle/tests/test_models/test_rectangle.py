#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init_with_positive_integers(self):
        r = Rectangle(4, 6, 3, 1, 12):
        self.assertEqual(r.width, 4)
