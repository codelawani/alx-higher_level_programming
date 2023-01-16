#!/usr/bin/python3
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import unittest
import os


class TestBase(unittest.TestCase):
    def setUp(self) -> None:
        Base._Base__nb_objects = 0
        return super().setUp()

    def test_init_without_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_init_with_id(self):
        b = Base(3)
        self.assertEqual(b.id, 3)

    def test_init_negative_id(self):
        b = Base(-2)
        self.assertEqual(b.id, -2)

    def test_init_with_string(self):
        b = Base('a')
        self.assertIsInstance(b.id, str)

    def test_init_with_None(self):
        b2 = Base(None)
        self.assertEqual(b2.id, 1)


class TestToJsonString(unittest.TestCase):
    def test_valid_input(self):
        print('test_valid_input')
        list_dictionaries = [{'x': 1, 'y': 2}, {'a': 3, 'b': 4}]
        expected_output = json.dumps(list_dictionaries)
        self.assertEqual(Base.to_json_string(
            list_dictionaries), expected_output)

    def test_empty_input(self):
        print('test_empty_input')
        list_dictionaries = []
        expected_output = '[]'
        self.assertEqual(Base.to_json_string(
            list_dictionaries), expected_output)

    def test_none_input(self):
        print('test_None_input')
        list_dictionaries = None
        expected_output = '[]'
        self.assertEqual(Base.to_json_string(
            list_dictionaries), expected_output)


class TestFromJsonString(unittest.TestCase):
    def test_valid_input(self):
        print('test_valid_input')
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_string = json.dumps(list_input)
        expected_output = [{'height': 4, 'width': 10, 'id': 89}, {
            'height': 7, 'width': 1, 'id': 7}]
        self.assertEqual(Base.from_json_string(json_string), expected_output)

    def test_empty_input(self):
        print('test_empty_input')
        json_input = ''
        expected_output = []
        self.assertEqual(Base.from_json_string(json_input), expected_output)

    def test_none_input(self):
        print('test_none_input')
        json_input = None
        expected_output = []
        self.assertEqual(Base.from_json_string(json_input), expected_output)
        """ with self.assertRaises(TypeError):
            Base.from_json_string(json_input) """
