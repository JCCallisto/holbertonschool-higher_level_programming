#!/usr/bin/python3

"""Module that contains the BaseGeometry class"""


class BaseGeometry:
    """A geometry class with area method and integer validation"""
    
    def area(self):
        """Raises an exception indicating area() is not implemented"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validates that value is a positive integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
