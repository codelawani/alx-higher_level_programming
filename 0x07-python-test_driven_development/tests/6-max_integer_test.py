#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        self.assertEqual(max_integer([1]), 1)

    def test_maximum_at_beginning(self):
        self.assertEqual(max_integer([3, 2, 1]), 3)

    def test_maximum_at_end(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_maximum_in_middle(self):
        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_all_elements_same(self):
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_negative_maximum(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_mixed_positive_and_negative_maximum_positive(self):
        self.assertEqual(max_integer([-1, 2, -3]), 2)

    def test_mixed_positive_and_negative_maximum_negative(self):
        self.assertEqual(max_integer([-3, -2, -1]), -1)
    def test_list_with_large_number_of_elements(self):
        # Test the function with a list containing a large number of elements
        self.assertEqual(max_integer([-5, 0, 3, -1, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), 20)

def test_list_with_mixed_data_types(self):
        # Test the function with a list containing a mix of different data types
        with self.assertRaises(TypeError):
            max_integer([-5, 0, 3, -1, 2, 'a', 'b', 'c'])


def test_list_with_infinite_values(self):
        # Test the function with a list containing a mix of positive, negative, and infinite values
        self.assertEqual(max_integer([-5, 0, 3, -1, 2, float('inf')]), float('inf'))

def test_list_with_complex_numbers(self):
        # Test the function with a list containing a mix of positive, negative, and complex numbers
        with self.assertRaises(TypeError):
            max_integer([-5, 0, 3, -1, 2, 3+4j, 5+6j])

def test_list_with_complex_numbers(self):
        # Test the function with a list containing a mix of positive, negative, and complex numbers
        with self.assertRaises(TypeError):
            max_integer([-5, 0, 3, -1, 2, 3+4j, 5+6j])
