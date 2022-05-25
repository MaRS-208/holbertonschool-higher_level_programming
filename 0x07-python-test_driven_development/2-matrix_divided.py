#!/usr/bin/python3
"""
    module
"""


def matrix_divided(matrix, div):
    """ divides a matrix """
    cpy = []
    for i in matrix:
        cpy.append(i[:])
    if not type(div) in[int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) != list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    l = len(matrix[0])
    for i in range(len(matrix)):
        if len(matrix[i]) != l:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for j in range (len(matrix[i])):
            cpy[i][j] = round(matrix[i][j] / div, 2)
    return cpy
