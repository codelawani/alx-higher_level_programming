#!/usr/bin/python3
from models.rectangle import Rectangle
import json
import unittest
import os
import io
import unittest.mock


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
        r2 = Rectangle(3, 2)
        self.assertEqual(r2.area(), 6)

    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), '[Rectangle] (12) 2/1 - 4/6')
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(r2.__str__(), f'[Rectangle] ({r2.id}) 1/0 - 5/5')

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

        r1.update(x=1, height=2, y=3, width=4, id=7)
        self.assertEqual(r1.id, 7)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 3)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display(self, mock_stdout):
        r1 = Rectangle(2, 3, 2, 2)
        r1.display()
        output = mock_stdout.getvalue()
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(output, expected_output)


class SaveToFile(unittest.TestCase):
    def test_valid_input_Rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        filename = f"Rectangle.json"
        self.assertTrue(os.path.isfile(filename))
        with open(filename, 'r') as f:
            json_str = f.read()
        list_of_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertEqual(json.loads(json_str), list_of_dicts)
        os.remove(filename)

    def test_empty_input(self):
        Rectangle.save_to_file([])
        filename = f"Rectangle.json"
        self.assertTrue(os.path.isfile(filename))
        with open(filename, 'r') as f:
            json_str = f.read()
        self.assertEqual(json_str, '[]')
        os.remove(filename)

    def test_none_input(self):
        Rectangle.save_to_file(None)
        filename = f"Rectangle.json"
        self.assertTrue(os.path.isfile(filename))
        with open(filename, 'r') as f:
            json_str = f.read()
        self.assertEqual(json_str, '[]')
        os.remove(filename)


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


class TestLoadFromFile(unittest.TestCase):
    def test_valid_input(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        filename = f"{Rectangle.__name__}.json"
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists(filename))
        with open(filename) as f:
            output = json.load(f)
        expected_output = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertEqual(output, expected_output)
        try:
            list_rect_output = Rectangle.load_from_file()
            self.assertEqual(r1.__str__(), list_rect_output[0].__str__())
            self.assertEqual(r2.__str__(), list_rect_output[1].__str__())
        except (FileNotFoundError):
            exit
        os.remove(filename)
