#!/usr/bin/env python3

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass

class Circle(Shape):
    """Circle class that inherits from Shape."""

    def __init__(self, radius):
        """Initialize a circle with the given radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """Rectangle class that inherits from Shape."""

    def __init__(self, width, height):
        """Initialize a rectangle with the given width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

def shape_info(shape):
    """Print the area and perimeter of a shape using duck typing."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
