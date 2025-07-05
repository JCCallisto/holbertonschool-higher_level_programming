#!/usr/bin/python3

"""Module that contains the is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of,
    or inherited from, the specified class"""
    return isinstance(obj, a_class)
