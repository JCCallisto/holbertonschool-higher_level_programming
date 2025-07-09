#!/usr/bin/python3

"""
Module that contains a function to load an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file

    Args:
        filename (str): The name of the JSON file to load from

    Returns:
        object: Python data structure loaded from the JSON file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
