def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False


def square_even_number(b):
    array = []
    for i in range(len(b)):
        if is_even(b[i]):
            array.append(b[i] ** 2)

    return array


print(square_even_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
