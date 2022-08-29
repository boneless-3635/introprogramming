def is_even(a):
    """
    check if integer is even
    :param a: a number (int)
    :return: true if even
    """
    if a % 2 == 0:
        return True
    else:
        return False


def square_odd_number(num_list):
    """
    square odd number within a comma separated string
    :param num_list: string with integers that are comma separated
    :return: list
    """
    array = []      # create an empty array
    list_int = [int(x) for x in num_list.split(",")]        # split the string with comma into a list containing integer

    for i in range(len(list_int)):      # traverse list
        if not is_even(list_int[i]):        # find odd number
            array.append(list_int[i] ** 2)      # square and append to the list

    return array


print(square_odd_number("1,2,3,4,5,6,7,8,9"))
