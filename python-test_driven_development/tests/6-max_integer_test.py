#!/usr/bin/python3

"""Unittest for max_integer function"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_regular_list(self):
        """Test with a regular list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_single_element(self):
        """Test with a single element list"""
        self.assertEqual(max_integer([7]), 7)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([-5]), -5)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -5, -1, -8]), -1)

    def test_mixed_numbers(self):
        """Test with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 0, 1]), 1)
        self.assertEqual(max_integer([-10, -5, 0, 5, 10]), 10)
        self.assertEqual(max_integer([5, -3, 8, -1, 2]), 8)

    def test_duplicate_max(self):
        """Test with duplicate maximum values"""
        self.assertEqual(max_integer([1, 2, 3, 3]), 3)
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([1, 5, 3, 5, 2]), 5)

    def test_max_at_beginning(self):
        """Test with maximum at the beginning"""
        self.assertEqual(max_integer([5, 1, 2, 3]), 5)
        self.assertEqual(max_integer([10, 1, 5, 3]), 10)

    def test_max_at_middle(self):
        """Test with maximum in the middle"""
        self.assertEqual(max_integer([1, 2, 10, 3, 4]), 10)
        self.assertEqual(max_integer([1, 15, 3, 2]), 15)

    def test_max_at_end(self):
        """Test with maximum at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4, 10]), 10)
        self.assertEqual(max_integer([5, 3, 1, 8]), 8)

    def test_large_numbers(self):
        """Test with large numbers"""
        self.assertEqual(max_integer([1000000, 999999, 1000001]), 1000001)
        self.assertEqual(max_integer([123456789, 987654321]), 987654321)

    def test_all_same_numbers(self):
        """Test with all identical numbers"""
        self.assertEqual(max_integer([7, 7, 7, 7, 7]), 7)
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer([-3, -3, -3]), -3)

    def test_two_elements(self):
        """Test with exactly two elements"""
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([2, 1]), 2)
        self.assertEqual(max_integer([-1, -2]), -1)

    def test_float_integers(self):
        """Test with float numbers that are integers"""
        self.assertEqual(max_integer([1.0, 2.0, 3.0]), 3.0)
        self.assertEqual(max_integer([5.0, 1.0]), 5.0)


if __name__ == '__main__':
    unittest.main()
