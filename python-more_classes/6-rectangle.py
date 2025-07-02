#!/usr/bin/python3
"""
Rectangle module - With instance counting

This module extends the Rectangle class to track the number of
Rectangle instances currently in existence using a class attribute.
"""


class Rectangle:
    """
    A Rectangle class with instance counting functionality.
    
    This class tracks the number of Rectangle instances currently in existence
    using a class attribute that is incremented on creation and decremented
    on destruction.
    
    Class Attributes:
        number_of_instances (int): Counter for the number of Rectangle 
            instances currently in existence.
    
    Instance Attributes:
        width (int): The width of the rectangle. Must be a non-negative integer.
        height (int): The height of the rectangle. Must be a non-negative integer.
    """
    
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance and increment the instance counter.

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
            >>> Rectangle.number_of_instances
            0
            >>> rect1 = Rectangle(3, 4)
            >>> Rectangle.number_of_instances
            1
            >>> rect2 = Rectangle(5, 2)
            >>> Rectangle.number_of_instances
            2
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

        Examples:
            >>> rect = Rectangle(5, 3)
            >>> rect.area()
            15
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
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return a string representation of the rectangle using '#' characters.

        Returns:
            str: A visual representation of the rectangle using '#' characters.
                Returns an empty string if width or height is 0.

        Examples:
            >>> rect = Rectangle(3, 2)
            >>> print(rect)
            ###
            ###
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = []
        for i in range(self.__height):
            rectangle.append('#' * self.__width)
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
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Destructor that decrements the instance counter and prints a farewell message.

        This method is automatically called when the object is garbage collected.
        It decrements the number_of_instances counter and prints a farewell message.

        Note:
            Each time a Rectangle is destroyed, the class attribute 
            number_of_instances is decremented by 1.

        Examples:
            >>> rect1 = Rectangle(3, 4)
            >>> rect2 = Rectangle(5, 2)
            >>> Rectangle.number_of_instances
            2
            >>> del rect1
            Bye rectangle...
            >>> Rectangle.number_of_instances
            1
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
