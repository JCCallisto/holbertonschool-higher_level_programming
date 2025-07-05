#!/usr/bin/python3

"""Module that contains the Square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize a Square with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
