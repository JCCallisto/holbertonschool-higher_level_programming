#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.

    Args:
        matrix: A 2 dimensional array

    Returns:
        A new matrix with same size as input matrix,
        where each value is the square of the input value
    """

    new_matrix = []

    for row in matrix:

        new_row = []
        for element in row:
            new_row.append(element ** 2)
        new_matrix.append(new_row)

    return new_matrix
