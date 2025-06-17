#!/usr/bin/python3

"""
Module for name formatting and display.

This module contains a function to print a formatted name string.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a formatted name string.

    Args:
        first_name (str): The first name to display. Must be a string.
        last_name (str, optional): The last name to display. Defaults to empty string.
                                  Must be a string if provided.

    Returns:
        None: This function prints the formatted name and doesn't return a value.

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.

    Examples:
        >>> say_my_name("John", "Smith")
        My name is John Smith
        
        >>> say_my_name("Bob")
        My name is Bob 
        
        >>> say_my_name("Alice", "Johnson")
        My name is Alice Johnson
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
