#!/usr/bin/python3

"""
Module that contains a Student class
"""


class Student:
    """
    Class that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantiation with first_name, last_name and age

        Args:
            first_name (str): The student's first name
            last_name (str): The student's last name
            age (int): The student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance

        Returns:
            dict: Dictionary representation of the student
        """
        return self.__dict__
