#!/usr/bin/python3
"""
Rectangle module - Complete implementation with class method

This module provides the complete Rectangle class implementation with
all features including a class method for creating square rectangles.
"""


class Rectangle:
    """
    A complete Rectangle class with comprehensive functionality.

    This class provides methods to create rectangles, calculate their area
    and perimeter, visualize them using ASCII characters, track instance count,
    compare rectangles, and create squares using a class method.

    Class Attributes:
        number_of_instances (int): Counter for the number of Rectangle
            instances currently in existence.
        print_symbol (str): Symbol used for printing the rectangle
            representation. Default is "#".

    Instance Attributes:
        width (int): The width of the rectangle.
        Must be a non-negative integer.
        height (int): The height of the rectangle.
        Must be a non-negative integer.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is negative.

        Note:
            Each time a Rectangle is created, the class attribute
            number_of_instances is incremented by 1.

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
        Rectangle.number_of_instances += 1

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
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
            Returns 0 if either
                width or height is 0, otherwise returns 2 × (width + height).

        Examples:
            >>> rect = Rectangle(5, 3)
            >>> rect.perimeter()
            16

            >>> rect = Rectangle(0, 5)
            >>> rect.perimeter()
            0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return a string representation of the rectangle using print symbols.

        Returns:
            str: A visual representation of the rectangle using
            the print_symbol character.
            Returns an empty string if width or height is 0.

        Examples:
            >>> rect = Rectangle(3, 2)
            >>> print(rect)
            ###
            ###

            >>> rect = Rectangle(0, 2)
            >>> print(rect)

        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = []
        for i in range(self.__height):
            rectangle.append(str(self.print_symbol) * self.__width)
        return '\n'.join(rectangle)

    def __repr__(self):
        """
        Return a string representation that can be used to recreate the object.

        Returns:
            str: A string in the format "Rectangle(width, height)".

        Examples:
            >>> rect = Rectangle(5, 3)
            >>> repr(rect)
            'Rectangle(5, 3)'

            >>> rect = Rectangle()
            >>> repr(rect)
            'Rectangle(0, 0)'
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Destructor called when the Rectangle instance is about to be destroyed.

        Decrements the class instance counter and prints a farewell message.
        This method is automatically called when the object
        is garbage collected.

        Examples:
            >>> rect = Rectangle(5, 3)
            >>> del rect
            Bye rectangle...
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare two rectangles and return the one with the
        larger or equal area.

        This static method compares two Rectangle instances based
        on their areas and returns the one with the larger area.
        If areas are equal, returns the first rectangle.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Returns:
            Rectangle: The rectangle with the larger or equal area.

        Raises:
            TypeError: If either argument is not a Rectangle instance.

        Examples:
            >>> rect1 = Rectangle(5, 3)  # area = 15
            >>> rect2 = Rectangle(4, 4)  # area = 16
            >>> bigger = Rectangle.bigger_or_equal(rect1, rect2)
            >>> bigger is rect2
            True

            >>> rect3 = Rectangle(3, 5)  # area = 15
            >>> bigger = Rectangle.bigger_or_equal(rect1, rect3)
            >>> bigger is rect1
            True
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Create a square Rectangle using a class method.

        This class method provides a convenient way to create square rectangles
        where width and height are equal. It returns a new Rectangle instance
        with both dimensions set to the specified size.

        Args:
            size (int, optional): The size of each side of the square.
            Defaults to 0.

        Returns:
            Rectangle: A new Rectangle instance with width and height
            both set to size.

        Raises:
            TypeError: If size is not an integer
            (raised by Rectangle.__init__).
            ValueError: If size is negative (raised by Rectangle.__init__).

        Examples:
            >>> square = Rectangle.square(4)
            >>> print(square.width, square.height)
            4 4
            >>> square.area()
            16

            >>> small_square = Rectangle.square(2)
            >>> print(small_square)
            ##
            ##

            >>> empty_square = Rectangle.square()
            >>> print(empty_square.width, empty_square.height)
            0 0

            >>> # Equivalent to Rectangle.square(3)
            >>> manual_square = Rectangle(3, 3)
            >>> auto_square = Rectangle.square(3)
            >>> manual_square.area() == auto_square.area()
            True
        """
        return cls(size, size)
