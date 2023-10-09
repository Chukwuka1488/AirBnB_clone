#!/usr/bin/env python3

"""
Module containing the Rectangle class to calculate the area of a rectangle.
"""

class Rectangle:
    """
    Represents a Rectangle with a width and height.

    Methods:
    - area(): Calculate and return the area of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle.

        Parameters:
        - width (float): The width of the rectangle.
        - height (float): The height of the rectangle.

        Raises:
        - ValueError: If width or height are negative.
        """
        if width < 0 or height < 0:
            raise ValueError("Width and height must be non-negative.")
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

# Example usage
if __name__ == "__main__":
    rectangle = Rectangle(5.0, 10.0)
    print(f"""
    The area of the rectangle with width {rectangle.width}
    and height {rectangle.height} is {rectangle.area()}""")
