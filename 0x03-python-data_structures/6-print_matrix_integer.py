#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            tmp = matrix[i][j]
            print("{:d}".format(tmp), end=" " if tmp != matrix[i][-1] else "")
        print()
