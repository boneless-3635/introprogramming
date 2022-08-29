def plus(a, b):
    """
    add a to a for b number of times
    :param a: number to add (int)
    :param b: number of times (int)
    :return: result of addition
    """
    if b == 1:
        return a
    else:
        return plus(a, b - 1) + a       # add a to a


print(plus(4, 6))
