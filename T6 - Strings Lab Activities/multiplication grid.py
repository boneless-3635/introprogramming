def multiplication_table(a, b):
    """
    creating a multiplication grid
    :param a: row of grid
    :param b: column of grid
    :return:
    """
    print("x".rjust(4), end="\t")
    for k in range(b + 1):
        print(str(k).rjust(4), end="\t")
    print("\n")
    for i in range(a + 1):
        print(str(i).rjust(4), end="\t")
        for j in range(b + 1):
            print(str(i * j).rjust(4), end="\t")
        print("\n")


c = int(input("Enter your row number: "))
d = int(input("Enter your column number: "))
multiplication_table(c, d)
