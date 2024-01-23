#!/usr/bin/python3
"""A module that contains matrix_divided matrix"""

def matrix_divided(matrix, div):
    """Divides all elements of a matrix.
    Args: matrix (list of lists): matrix to be divided.
          div (int or float): number to divide the matrix by.
    Returns: new_matrix (list of lists): new matrix with quotients.
    """
    new_matrix = []
    error_msgs = ["matrix must be a matrix (list of lists) of integers/floats",
                  "Each row of the matrix must have the same size",
                  "div must be a number",
                  "division by zero"]
    if type(matrix) is not list:
        raise TypeError(error_msgs[0])
    list_length = len(matrix)
    for i in range(list_length):
        quotients_list = []
        for j in range(len(matrix[i])):
            element = matrix[i][j]
            if i != list_length - 1:
                if len(matrix[i]) != len(matrix[i + 1]):
                    raise TypeError(error_msgs[1])
            if type(div) is not int and type(div) is not float:
                raise TypeError(error_msgs[2])
            if div == 0:
                raise ZeroDivisionError(error_msgs[3])
            if type(element) is not int and type(element) is not float:
                raise TypeError(error_msgs[0])
            quotients_list.append(round(element / div, 2))
        new_matrix.append(quotients_list)
    return new_matrix
