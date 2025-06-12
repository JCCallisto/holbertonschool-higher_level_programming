#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order, one per line"""
    if my_list:
        for integer in reversed(my_list):
            print("{:d}".format(integer))
