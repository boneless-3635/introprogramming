def remove_specified_string(s, string2):
    """
    remove a string from a string
    :param s: original string
    :param string2: string that is removed
    :return: new string
    """
    new = ""
    for i in s:
        new = s.replace(string2, "")
    return new


print(remove_specified_string("expensive", "ex"))
