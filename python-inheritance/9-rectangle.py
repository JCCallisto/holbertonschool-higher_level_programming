#!/usr/bin/python3

"""Module that contains the Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a Rectangle with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
