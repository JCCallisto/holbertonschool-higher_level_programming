#!/usr/bin/python3

def max_integer(my_list=[]):
    """Find the biggest integer of a list"""
    if not my_list:
        return None

    max_value = my_list[0]
    for integer in my_list:
        if integer > max_value:
            max_value = integer

    return max_value
