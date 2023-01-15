#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_init_with_positive_integers(self):
        r = Rectangle(4, 6, 3, 1, 12)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 12)

    def test_init_negative_integers(self):
        self.assertRaises(ValueError, Rectangle, -4, 6)
        self.assertRaises(ValueError, Rectangle, 4, -6)
        self.assertRaises(ValueError, Rectangle, 4, 6, -2)
        self.assertRaises(ValueError, Rectangle, 4, 6, 2, -4)

    def test_init_with_string(self):
        with self.assertRaises(TypeError):
            Rectangle('a', 'b')

    def test_init_with_None(self):
        with self.assertRaises(TypeError):
            Rectangle(None, None)

    def test_area(self):
        r1 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 56)

    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), '[Rectangle] (12) 2/1 - 4/6')

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        assert r1.id == 89
        assert r1.width == 2
        assert r1.height == 3
        assert r1.x == 4
        assert r1.y == 5
        r1.update(x=1, height=2, y=3, width=4, id=7)
        assert r1.id == 7
        assert r1.width == 4
        assert r1.height == 2
        assert r1.x == 1
        assert r1.y == 3
