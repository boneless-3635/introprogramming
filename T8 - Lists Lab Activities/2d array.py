import numpy


def array_2d(row, column):
    """
    creating a 2d array with contents
    :param row: number of row
    :param column: number of column
    :return: 2d array
    """
    final_array = []        # creating the final array
    for i in range(row):        # traverse through rows
        array = []      # create rows
        for j in range(column):     # traverse through column
            array.append(i * j)     # content of array is row * column
        final_array.append(array)       # append many rows to create 2d array
    return final_array


def array_2d_alt(row, column):
    array = numpy.zeros([column, row])      # create final 2d array with column and row
    for i in range(row):        # traverse through row and column
        for j in range(column):
            array[i, j] = i * j     # content of array is row * column

    return array


print(array_2d_alt(5, 5))
