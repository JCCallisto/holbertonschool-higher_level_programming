#!/usr/bin/python3

"""
This module defines a Square class with size validation, area calculation,
and property getter/setter for size.
"""


class Square:
    """
    A class that defines a square with a private size attribute, validation,
    area calculation, and property access to size.
    """

    def __init__(self, size=0):
        """
        Initialize a Square instance.

        Args:
            size: The size of the square (default is 0)
        """
        self.size = size

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute with validation.

        Args:
            value: The new size value

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the current square area.
        
        Returns:
            int: The area of the square (size * size)
        """
        return self.__size * self.__size
