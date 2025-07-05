#!/usr/bin/python3

"""Module that contains the MyList class"""


class MyList(list):
    """A class that inherits from list with additional functionality"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
