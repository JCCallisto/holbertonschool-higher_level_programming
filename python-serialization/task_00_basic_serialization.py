#!/usr/bin/env python3
"""
Basic serialization module for Python dictionaries to JSON files.

This module provides functions to serialize Python dictionaries to JSON files
and deserialize JSON files back to Python dictionaries.
"""

import json
import os


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save it to a file.

    Args:
        data (dict): A Python dictionary containing the data to serialize
        filename (str): The filename of the output JSON file

    Returns:
        None

    Raises:
        TypeError: If data is not a dictionary
        IOError: If there's an error writing to the file
    """
    if not isinstance(data, dict):
        raise TypeError("Data must be a dictionary")

    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except IOError as e:
        raise IOError(f"Error writing to file '{filename}': {e}")


def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from a file to recreate a Python dictionary.

    Args:
        filename (str): The filename of the input JSON file

    Returns:
        dict: A Python dictionary with the deserialized JSON data

    Raises:
        FileNotFoundError: If the specified file doesn't exist
        json.JSONDecodeError: If the file contains invalid JSON
        IOError: If there's an error reading the file
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File '{filename}' not found")

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON in file '{filename}': {e}")
    except IOError as e:
        raise IOError(f"Error reading file '{filename}': {e}")


if __name__ == "__main__":
    data_to_serialize = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    serialize_and_save_to_file(data_to_serialize, 'data.json')
    print("Data serialized and saved to 'data.json'.")
    
    deserialized_data = load_and_deserialize('data.json')

    print("Deserialized Data:")
    print(deserialized_data)

    print(f"Data integrity check: {data_to_serialize == deserialized_data}")
