#!/usr/bin/python3

"""
Module for printing square patterns.

This module contains a function to print a square pattern using hash characters.
"""


def print_square(size):
    """
    Prints a square pattern using hash (#) characters.

    Args:
        size (int): The size of the square (width and height). Must be a non-negative integer.

    Returns:
        None: This function prints the square pattern and doesn't return a value.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is negative.

    Examples:
        >>> print_square = __import__('4-print_square').print_square
        >>> print_square(4)
        ####
        ####
        ####
        ####
        
        >>> print_square(1)
        #
        
        >>> print_square(0)
        
        >>> print_square(-1)
        Traceback (most recent call last):
            ...
        ValueError: size must be >= 0
        
        >>> print_square()
        Traceback (most recent call last):
            ...
        TypeError: print_square() missing 1 required positional argument: 'size'
        
        >>> print_square("3")
        Traceback (most recent call last):
            ...
        TypeError: size must be an integer
        
        >>> print_square(3.5)
        Traceback (most recent call last):
            ...
        TypeError: size must be an integer
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
