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
        >>> print_square(3)
        ###
        ###
        ###
        
        >>> print_square(1)
        #
        
        >>> print_square(0)
        
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
