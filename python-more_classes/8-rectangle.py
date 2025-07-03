#!/usr/bin/python3
"""
Rectangle module - With static comparison method

This module extends the Rectangle class to include a static method
for comparing two rectangles based on their areas.
"""


class Rectangle:
    """
    A Rectangle class with static comparison method.

    This class includes all previous functionality plus a static method
    to compare two Rectangle instances based on their areas and return
    the one with the larger or equal area.

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
        Initialize a new Rectangle instance and increment the instance counter.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is negative.
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
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle. Returns 0 if either
                width or height is 0, otherwise returns 2 × (width + height).
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return a string representation using the current print_symbol.

        Returns:
            str: A visual representation of the rectangle
            using the print_symbol.
                Returns an empty string if width or height is 0.
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
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Destructor that decrements the instance counter and prints a farewell message.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare two rectangles and return the one with
        the larger or equal area.

        This static method compares two Rectangle instances based on their 
        areas and returns the one with the larger area. If areas are equal,
        returns the first rectangle.

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

            >>> rect4 = Rectangle(2, 6)  # area = 12
            >>> bigger = Rectangle.bigger_or_equal(rect1, rect4)
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
