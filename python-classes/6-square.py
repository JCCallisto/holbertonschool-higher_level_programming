#!/usr/bin/python3

"""
This module defines a Square class with size validation, area calculation,
property getter/setter for size and position, and positioned visual printing.
"""


class Square:
    """
    A class that defines a square with private size and position attributes,
    validation, area calculation, property access, and positioned visual printing.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a Square instance.

        Args:
            size: The size of the square (default is 0)
            position: The position of the square (default is (0, 0))
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter for the position attribute.

        Returns:
            tuple: The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position attribute with validation.

        Args:
            value: The new position value

        Raises:
            TypeError: If position is not a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(i, int) for i in value) or
            not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the current square area.

        Returns:
            int: The area of the square (size * size)
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square with the character '#' at the specified position.
        If size is 0, print an empty line.
        Position is used by adding spaces before the square.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()

            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
