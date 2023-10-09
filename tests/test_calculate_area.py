#!/usr/bin/env python3

import unittest
from calculate_area import Rectangle

class TestRectangleArea(unittest.TestCase):
    """
    Test cases for the Rectangle class in the calculate_area module.
    """

    def test_area(self):
        """
        Test the area method of the Rectangle class.
        """
        rectangle = Rectangle(5.0, 10.0)
        self.assertEqual(rectangle.area(), 50.0)

    def test_negative_width(self):
        """
        Test that a ValueError is raised when the width is negative.
        """
        with self.assertRaises(ValueError):
            rectangle = Rectangle(-5.0, 10.0)

    def test_negative_height(self):
        """
        Test that a ValueError is raised when the height is negative.
        """
        with self.assertRaises(ValueError):
            rectangle = Rectangle(5.0, -10.0)

    def test_negative_width_and_height(self):
        """
        Test that a ValueError is raised when both width and height are negative.
        """
        with self.assertRaises(ValueError):
            rectangle = Rectangle(-5.0, -10.0)


if __name__ == "__main__":
    unittest.main()
