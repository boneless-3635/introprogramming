def calculate_harmonic_series(n):
    """
    calculate the nth number in the harmonic series
    :param n: the nth number (int)
    :return: value of the series
    """
    if n == 1:
        return 1.0
    else:
        return 1 / n + calculate_harmonic_series(n-1)


harmonic_number = int(input("Input the harmonic series number: "))
print(round(calculate_harmonic_series(harmonic_number), 3))
