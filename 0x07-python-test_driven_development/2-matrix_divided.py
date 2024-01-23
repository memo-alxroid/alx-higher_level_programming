#!/usr/bin/python3

def matrix_divided(matrix, div):
    """Divides all elements of a matrix.
    Args: matrix (list of lists): matrix to be divided.
          div (int or float): number to divide the matrix by.
    Returns: new_matrix (list of lists): new matrix with quotients.
    """
    new_matrix = []
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    list_length = len(matrix)
    for i in range(list_length):
        quotients_list = []
        for j in range(len(matrix[i])):
            if i != list_length - 1:
                if len(matrix[i]) != len(matrix[i + 1]):
                    raise TypeError("Each row of the matrix must have the same size")
            if type(div) is not int and type(div) is not float:
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            if type(matrix[i][j]) is not int and type(matrix[i][j]) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            quotients_list.append(round(matrix[i][j] / div, 2))
        new_matrix.append(quotients_list)
    return new_matrix
