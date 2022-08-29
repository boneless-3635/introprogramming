def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def is_odd(num):
    if not is_even(num):
        return True
    else:
        return False


a = int(input("Enter your number: "))
print(is_odd(a))
