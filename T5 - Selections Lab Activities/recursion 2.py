def squared_sum(n):
    total = 0
    for i in range(n+1):
        total = total + i ** 2
    return total


def squared_sum_recursion(n):
    """
    sum of squared that number and decreasing towards 1
    :param n: number (int)
    :return: the sum
    """
    total = 0
    if n == 1:
        return 1
    else:
        return n ** 2 + squared_sum_recursion(n - 1)


print(squared_sum_recursion(2))
