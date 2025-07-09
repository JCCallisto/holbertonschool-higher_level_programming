#!/usr/bin/env python3
"""
Custom object serialization module using pickle.

This module provides a CustomObject class that can serialize and deserialize
itself using Python's pickle module.
"""

import pickle
import os


class CustomObject:
    """
    A custom class that demonstrates pickle serialization and deserialization.

    Attributes:
        name (str): The name of the object
        age (int): The age of the object
        is_student (bool): Whether the object represents a student
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.

        Args:
            name (str): The name of the object
            age (int): The age of the object
            is_student (bool): Whether the object represents a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Print the object's attributes in a formatted manner.

        Returns:
            None
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.

        Args:
            filename (str): The name of the file to save the serialized object to

        Returns:
            None
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a CustomObject instance from a file using pickle.

        Args:
            filename (str): The name of the file to load the serialized object from

        Returns:
            CustomObject: The deserialized CustomObject instance, or None if error occurs
        """
        try:
            if not os.path.exists(filename):
                return None

            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                return obj
        except Exception:
            return None


if __name__ == "__main__":
    obj = CustomObject(name="John", age=25, is_student=True)
    print("Original Object:")
    obj.display()

    obj.serialize("object.pkl")

    new_obj = CustomObject.deserialize("object.pkl")
    print("\nDeserialized Object:")
    new_obj.display()