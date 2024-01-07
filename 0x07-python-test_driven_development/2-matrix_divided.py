#!/usr/bin/python3
"""
 Function that divides all
 elements of a matrix.
"""


def matrix_divided(matrix, div):
    """ Returns the matrix divided by div. """
    if not isinstance(matrix, list) or not matrix:
        raise TypeError("matrix must be a matrix"
                        "(list of lists)of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix"
                            "(list of lists) of integers/floats")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix"
                                "(list of lists) of integers/floats")
    first_row = len(matrix[0])
    for row in matrix[1:]:
        if len(row) != first_row:
            raise TypeError("Each row of the matrix must have the same size")
    if (not isinstance(div, int) and not isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)
    return new_matrix
