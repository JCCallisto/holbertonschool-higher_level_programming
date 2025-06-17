#!/usr/bin/python3

"""
Module for matrix division operations.

This module contains a function to
divide all elements of a matrix by a given divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix (list): A matrix (list of lists) containing integers or floats.
                      All rows must have the same size.
        div (int or float): The divisor to divide each element by.
                           Must not be zero.

    Returns:
        list: A new matrix with all elements divided by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                  if rows have different sizes, or if div is not a number.
        ZeroDivisionError: If div is zero.

    Examples:
        >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

        >>> matrix_divided([[10, 20], [30, 40]], 2)
        [[5.0, 10.0], [15.0, 20.0]]
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    if not matrix:
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix "
                            "must have the same size")

    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix
