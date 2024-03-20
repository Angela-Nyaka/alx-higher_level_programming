#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy_matrix = []

    for row in matrix:
        copy_matrix.append(list(map(lambda x: x * x, row)))
    return (copy_matrix)
