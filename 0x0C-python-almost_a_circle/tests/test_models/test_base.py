#!/usr/bin/python3
from models.base import Base
from models.rectangle import Rectangle
import json
import unittest
import os


class TestBase(unittest.TestCase):

    def test_init_without_id(self):
        print('test_init_without_id')
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 2)
        self.assertEqual(b2.id, 3)

    def test_init_with_id(self):
        print('test_init_with_id')
        b = Base(3)
        self.assertEqual(b.id, 3)

    def test_init_negative_id(self):
        print('test_init_negative_id')
        b = Base(-2)
        self.assertEqual(b.id, -2)

    def test_init_with_string(self):
        print('test_init_with_string')
        b = Base('a')
        self.assertEqual(b.id, 'a')

    def test_init_with_None(self):
        print('test_init_with_None')
        b = Base(None)
        self.assertEqual(b.id, 1)


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
        expected_output = '"[]"'
        self.assertEqual(Base.to_json_string(
            list_dictionaries), expected_output)

    def test_none_input(self):
        print('test_None_input')
        list_dictionaries = None
        expected_output = '"[]"'
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


class TestCreate(unittest.TestCase):
    def test_valid_input(self):
        r1 = Rectangle(4, 6, 1, 2, 1)
        r1_dictionary = r1.to_dictionary()
        newInstance = Rectangle.create(**r1_dictionary)
        assert newInstance.width == 4
        assert newInstance.height == 6
        assert newInstance.x == 1
        assert newInstance.y == 2
        assert newInstance.id == 1
        self.assertIsNot(r1, newInstance)
        self.assertNotEqual(r1, newInstance)


class SaveToFile(unittest.TestCase):
    def test_valid_input(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        filename = f"Rectangle.json"
        self.assertTrue(os.path.isfile(filename))
