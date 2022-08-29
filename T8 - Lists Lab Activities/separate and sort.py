def sort_words(word_list):
    """
    sort a string with comma separated words
    :param word_list: list of words as a string
    :return: list
    """
    split_word = word_list.split(",")       # split the words in a string into a list

    for i in range(1, len(split_word)):     # insertion sort algorithm
        key = split_word[i]
        j = i - 1
        while j >= 0 and key < split_word[j]:
            split_word[j + 1] = split_word[j]
            j -= 1
        split_word[j + 1] = key

    return split_word


print(sort_words("without,hello,bag,world"))
