#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = [[i ** 2 for i in j] for j in matrix]
    return square_matrix
