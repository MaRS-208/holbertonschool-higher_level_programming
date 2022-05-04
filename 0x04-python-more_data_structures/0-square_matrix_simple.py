#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for y in matrix:
        new_list = list(map(lambda x: x * x, y))
        new_matrix.append(new_list)
    return new_matrix
