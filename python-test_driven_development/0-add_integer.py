#!/usr/bin/python3

"""
This module provides a function to add two integers.

The module contains a single function add_integer that takes two numeric
arguments and returns their sum as an integer.
"""

def add_integer(a, b=98):
    """
    Add two integers together.
    
    This function takes two numeric values (int or float) and returns their
    sum as an integer. Float values are cast to integers before addition.
    
    Args:
        a (int or float): The first number to add
        b (int or float, optional): The second number to add. Defaults to 98.
    
    Returns:
        int: The sum of a and b as an integer
    
    Raises:
        TypeError: If a or b is not an integer or float
        OverflowError: If a float value is infinity
        ValueError: If a float value is NaN
    
    Examples:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
        >>> add_integer(2)
        100
        >>> add_integer(100.3, -2)
        98
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast to integers if they are floats
    a = int(a)
    b = int(b)

    return a + b
