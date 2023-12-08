#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    newMatrix = matrix.copy()
    newMatrix = [[lists[i] * lists[i] for i in range(len(lists))]
                 for lists in matrix]
    return newMatrix
