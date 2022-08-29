def translate_eng2pirate(s):
    """
    Translate english to pirate
    :param s: string to translate as a list
    :return: translated string
    """
    f = open("eng2pirate.txt", "r")
    lines = f.readlines()
    dict_trans = {}
    for line in lines:
        line = line.split("\t")
        eng_word = line[0].lower().strip()
        pir_word = line[-1].lower().strip()
        dict_trans[eng_word] = pir_word

    translated_string = ""

    for word in s:
        if word in dict_trans:
            translated_string += dict_trans[word] + " "
        else:
            translated_string += word + " "

    return translated_string

    # reverse_pirate_dict = {value:key for key,value in pirate_dict.items()}


# main program
sentence = input("Please enter your sentence: ")
sentence = sentence.lower().split(" ")
print(translate_eng2pirate(sentence))




