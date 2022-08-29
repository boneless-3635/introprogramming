def collatz_sequence(a):
    number = list()
    number.append(a)        # add starting integer
    x = a       # placeholder number to calculate
    highest_int = 0

    if a == 1:      # number 1 has no steps
        number.append(0)
        highest_int = 0

    while x != 1:       # prevent x from getting to 1
        if x % 2 == 0:      # even number check
            x = int(x / 2)      # perform calculation
            number.append(x)       # add number to list

        else:
            x = 3 * x + 1       # perform calculation
            number.append(x)       # add number to list

        highest_int = max(highest_int, x)

    print("max_collatz(" + str(a) + ") ->", highest_int)      # print the highest number in the sequence
    print("Collatz sequence: ", number)     # print the sequence


def max_collatz(b):
    """
    Recursive function finds the largest number in the Collatz sequence
    :param b: a number (int)
    :return: max number of the sequence
    """
    if b == 1:
        return 1
    else:
        if b % 2 == 0:
            return max(b, max_collatz(b / 2))
        else:
            return max(b, max_collatz(b * 3 + 1))


collatz_sequence(85)
print(max_collatz(85))

