def find_triangular_numbers(n):
    """
    find triangular number
    :param n: the nth number of the triangular number (int)
    :return: the triangular number
    """
    if n == 1:
        return 1
    else:
        return n + find_triangular_numbers(n-1)


def print_triangular_number(n):
    for i in range(1, int(n) + 1):
        print(i, find_triangular_numbers(i))


print_triangular_number(5)
