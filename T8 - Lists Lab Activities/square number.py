def square_list():
    array = []
    for i in range(100):
        array.append((i + 1) ** 2)

    return array[-5:]


print(square_list())
