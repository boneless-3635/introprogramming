import re


def count_words(filename):
    """
    Count words from a text file
    :param filename: name of the file
    :return: list of words that are counted
    """
    book = open(filename, "r")
    dict_words = {}
    book_split = re.split(r"[-;,.\s]\s*", book.read().lower())

    for words in book_split:
        words = re.sub("[^a-zA-Z0-9 \-]", '', words)
        words_strip = words.strip()
        if words_strip not in dict_words:
            dict_words[words_strip] = 1
        else:
            dict_words[words_strip] += 1

    return dict_words


print(count_words("alice.txt"))
