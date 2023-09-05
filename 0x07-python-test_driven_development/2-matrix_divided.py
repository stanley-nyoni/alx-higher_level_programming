#!/usr/bin/python3

""" 
    Matrix divided
    Divides all elements of a matrix 
    Returns a new matrix
    
"""

def matrix_divided(matrix, div):
    """Divides all elements by div and return new matrix
        Raises exception in case div = 0
    """
    res_matrix = []
    for row in matrix:
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix(list of lists) of integers/floats")
    first_row_len = len(matrix[0])
    for row in matrix[1:]:
        if len(row) != first_row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        res_matrix.append(new_row)

    return res_matrix
