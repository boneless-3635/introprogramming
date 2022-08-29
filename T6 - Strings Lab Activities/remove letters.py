def remove_specified_letter(s, letter):
    new = ""
    for i in s:
        for j in letter:
            if i != j:
                new = new + i
    print(new)


def alt_remove_specified_letter(s, letter):
    """
    remove a letter from a string
    :param s: string
    :param letter: letter to be removed (string)
    :return: new letter
    """
    new = ""
    for i in s:
        new = s.replace(i, "")
    return new


print(alt_remove_specified_letter("expensive", "e"))
