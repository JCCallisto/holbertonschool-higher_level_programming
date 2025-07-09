#!/usr/bin/env python3
"""
XML serialization and deserialization module.

This module provides functionality to serialize Python dictionaries to XML format
and deserialize XML files back to Python dictionaries using the xml.etree.ElementTree module.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML format and save it to a file.

    Args:
        dictionary (dict): The Python dictionary to serialize
        filename (str): The filename to save the XML data to

    Returns:
        None
    """
    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file and return a Python dictionary.

    Args:
        filename (str): The filename of the XML file to read

    Returns:
        dict: A Python dictionary containing the deserialized XML data
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result_dict = {}

    for child in root:
        result_dict[child.tag] = child.text

    return result_dict


if __name__ == "__main__":
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)
