#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """ def setUp(self) -> None:
        self.s1 = Rectangle(8, 7, 0, 0, 12)
        return super().setUp() """

    def test_init_with_positive_integers(self):
        print('R:test_init_with_positive_integers')
        s = Square(4, 6, 3, 12)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.x, 6)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 12)

    def test_init_negative_integers(self):
        print('R:test_init_negative_integers')
        self.assertRaises(ValueError, Square, -4, 6)
        self.assertRaises(ValueError, Square, 4, -6)
        self.assertRaises(ValueError, Square, 4, 6, -2)

    def test_init_with_string(self):
        print('S:test_init_with_string')
        with self.assertRaises(TypeError):
            Square('a')

    def test_init_with_None(self):
        print('S:test_init_with_None')
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


""" class TestArea(unittest.TestCase):
    def test_ """
