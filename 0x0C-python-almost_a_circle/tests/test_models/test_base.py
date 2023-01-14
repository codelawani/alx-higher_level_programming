#!/usr/bin/python3
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_init_without_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base()
        self.assertEqual(b2.id, 3)

    def test_init_with_id(self):
        b = Base(3)
        self.assertEqual(b.id, 3)

    def test_init_negative_id(self):
        b = Base(-2)
        self.assertEqual(b.id, -2)

    def test_init_with_string(self):
        b = Base('a')
        self.assertEqual(b.id, 'a')

    def test_init_with_None(self):
        b = Base(None)
        self.assertEqual(b.id, 1)
