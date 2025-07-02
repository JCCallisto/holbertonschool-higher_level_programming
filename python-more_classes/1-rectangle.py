#!/usr/bin/python3
"""
Rectangle module - With properties and validation

This module provides a Rectangle class with proper encapsulation,
input validation, and getter/setter properties for width and height.
"""


class Rectangle:
    """
    A Rectangle class with validated width and height properties.
    
    This class implements proper encapsulation using private attributes
    and properties with validation to ensure width and height are
    non-negative integers.
    
    Attributes:
        width (int): The width of the rectangle. Must be a non-negative integer.
        height (int): The height of the rectangle. Must be a non-negative integer.
    """
    
    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is negative.

        Examples:
            >>> rect = Rectangle()
            >>> print(rect.width, rect.height)
            0 0
            
            >>> rect = Rectangle(5, 3)
            >>> print(rect.width, rect.height)
            5 3
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle with validation.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.

        Examples:
            >>> rect = Rectangle()
            >>> rect.width = 5
            >>> rect.width
            5
            
            >>> rect.width = -1  # Raises ValueError
            >>> rect.width = "5"  # Raises TypeError
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle with validation.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.

        Examples:
            >>> rect = Rectangle()
            >>> rect.height = 3
            >>> rect.height
            3
            
            >>> rect.height = -1  # Raises ValueError
            >>> rect.height = "3"  # Raises TypeError
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
