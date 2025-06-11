#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list"""
    result = []
    for integer in my_list:
        if integer % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
