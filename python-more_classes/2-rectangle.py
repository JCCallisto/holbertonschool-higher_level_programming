#!/usr/bin/python3
"""
Rectangle module - With area and perimeter calculations

This module extends the Rectangle class to include methods for
calculating the area and perimeter of the rectangle.
"""


class Rectangle:
    """
    A Rectangle class with validated properties and calculation methods.
    
    This class provides width and height properties with validation,
    along with methods to calculate the area and perimeter of the rectangle.
    
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
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle (width × height).

        Examples:
            >>> rect = Rectangle(5, 3)
            >>> rect.area()
            15
            
            >>> rect = Rectangle(0, 5)
            >>> rect.area()
            0
            
            >>> rect = Rectangle(4, 4)
            >>> rect.area()
            16
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle. Returns 0 if either 
                width or height is 0, otherwise returns 2 × (width + height).

        Examples:
            >>> rect = Rectangle(5, 3)
            >>> rect.perimeter()
            16
            
            >>> rect = Rectangle(0, 5)
            >>> rect.perimeter()
            0
            
            >>> rect = Rectangle(4, 4)
            >>> rect.perimeter()
            16
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
