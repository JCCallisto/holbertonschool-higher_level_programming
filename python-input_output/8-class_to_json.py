#!/usr/bin/python3

"""
Module that contains a function to convert a class instance to JSON dictionary
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object

    Args:
        obj: An instance of a Class

    Returns:
        dict: Dictionary representation of the object's attributes
    """
    return obj.__dict__
