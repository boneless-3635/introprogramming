def is_palindrome(s):
    """
    check if a string is palindrome
    :param s: string to check
    :return: true if palindrome
    """
    reversed_string = ""
    for i in s:
        reversed_string = i.lower() + reversed_string
    if reversed_string.lower() == s.lower():
        return True
    else:
        return False


print(is_palindrome("condo"))
