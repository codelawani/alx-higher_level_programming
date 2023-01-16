#!/usr/bin/python3
from models.rectangle import Rectangle
from models.square import Square
import json
import unittest
import os


class TestSquare(unittest.TestCase):
    """ def setUp(self) -> None:
        self.s1 = Rectangle(8, 7, 0, 0, 12)
        return super().setUp() """

    def test_init_with_positive_integers(self):
        s = Square(4, 6, 3, 12)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.x, 6)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 12)

    def test_init_negative_integers(self):
        self.assertRaises(ValueError, Square, -4, 6)
        self.assertRaises(ValueError, Square, 4, -6)
        self.assertRaises(ValueError, Square, 4, 6, -2)

    def test_init_with_string(self):
        with self.assertRaises(TypeError):
            Square('a')

    def test_init_with_None(self):
        with self.assertRaises(TypeError):
            Square(None)

    def test_area(self):
        s1 = Square(4, 6, 2, 12)
        self.assertEqual(s1.area(), 16)

    def test_str(self):
        s1 = Square(3, 1, 3, 9)
        self.assertEqual(s1.__str__(), '[Square] (9) 1/3 - 3')

    def test_update(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(89, 2, 3, 4)
        assert s1.id == 89
        assert s1.size == 2
        assert s1.x == 3
        assert s1.y == 4
        s1.update(x=1, y=3, size=4, id=7)
        assert s1.id == 7
        assert s1.size == 4
        assert s1.x == 1
        assert s1.y == 3

    def test_to_dictionary(self):
        s1 = Square(10, 2, 1, 1)
        s1_dictionary = s1.to_dictionary()
        expected_output = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s1_dictionary, expected_output)
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertEqual(s2.size, 10)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 1)
        self.assertIsNot(s1, s2)
        self.assertNotEqual(s1, s2)


class TestSaveToFile(unittest.TestCase):
    def test_empty_input(self):
        Square.save_to_file([])
        filename = f"Square.json"
        self.assertTrue(os.path.isfile(filename))
        with open(filename, 'r') as f:
            json_str = f.read()
        self.assertEqual(json_str, '[]')
        os.remove(filename)

    def test_none_input(self):
        Square.save_to_file(None)
        filename = f"Square.json"
        self.assertTrue(os.path.isfile(filename))
        with open(filename, 'r') as f:
            json_str = f.read()
        self.assertEqual(json_str, '[]')
        os.remove(filename)
