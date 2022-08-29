def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False


def filter_even_number(array):
    array2 = []
    for i in array:
        if is_even(int(i)):
            array2.append(i)

    return array2


print(filter_even_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
