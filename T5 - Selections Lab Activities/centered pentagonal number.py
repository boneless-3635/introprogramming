def find_centered_pentagonal_number(n):
    """
    find the nth centered pentagonal number
    :param n: first nth number (int)
    :return: the number
    """
    if n == 1:
        return 1
    else:
        return find_centered_pentagonal_number(n - 1) + (5 * (n - 1))   # previous number + 5 * prev


print(find_centered_pentagonal_number(4))
