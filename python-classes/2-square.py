#!/usr/bin/python3

"""
This module defines a Square class with size validation.
"""


class Square:
    """
    A class that defines a square with a private size attribute and validation.
    """

    def __init__(self, size=0):
        """
        Initialize a Square instance.

        Args:
            size: The size of the square (default is 0)

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
