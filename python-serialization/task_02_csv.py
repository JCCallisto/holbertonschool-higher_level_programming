#!/usr/bin/env python3
"""
CSV to JSON conversion module.

This module provides functionality to convert CSV files to JSON format
using Python's csv and json modules.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON format and save it to data.json.

    Args:
        csv_filename (str): The filename of the input CSV file

    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:
        data = []

        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False


if __name__ == "__main__":
    csv_file = "data.csv"
    if convert_csv_to_json(csv_file):
        print(f"Data from {csv_file} has been converted to data.json")
    else:
        print(f"Failed to convert {csv_file}")
