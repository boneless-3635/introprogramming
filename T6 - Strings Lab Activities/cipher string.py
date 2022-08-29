def cipher_string(s, mapping):
    """
    cipher a string using a key map
    :param s: string to be
    :param mapping:
    :return:
    """
    new = ""       # empty list for storing
    s = s.upper()
    mapping = mapping.upper()
    mapping_dictionary = {}     # creating a dictionary
    for i in range(65, 91):     # traverse from 65 to 91 which is the ascii value for capitalized alphabet letters
        mapping_dictionary[chr(i)] = mapping[i-65]      # key is the alphabet character and value is the cipher characters
    mapping_dictionary.update({" ": " "})
    list_keys = list(mapping_dictionary.keys())     # list for keys
    list_values = list(mapping_dictionary.values())     # list for values
    for j in s:     # traverse through original string
        for k in range(len(list_keys)):     # traverse through the list of values/keys
            if j == list_keys[k]:       # check if original string matches the key
                new += list_values[k]    # add the value of that key to the string
                break
    print(new)


def decipher_string(s, mapping):
    new = ""       # empty list for storing
    s = s.upper()
    mapping = mapping.upper()
    mapping_dictionary = {}     # creating a dictionary
    for i in range(65, 91):     # traverse from 65 to 91 which is the ascii value for capitalized alphabet letters
        mapping_dictionary[chr(i)] = mapping[i-65]      # key is the alphabet character and value is the cipher characters
    mapping_dictionary.update({" ": " "})
    list_keys = list(mapping_dictionary.keys())     # list for keys
    list_values = list(mapping_dictionary.values())     # list for values
    for j in s:     # traverse through original string
        for k in range(len(list_values)):     # traverse through the list of values/keys
            if j == list_values[k]:       # check if original string matches the key
                new += list_keys[k]    # add the value of that key to the string
                break
    print(new)


cipher_string("conversa tion", "QTGABCDEFHIJKLMNOPRSUVXYZW")
decipher_string("GMLVBPRQ SFML", "QTGABCDEFHIJKLMNOPRSUVXYZW")

cipher_key = 'QTGABCDEFHIJKOMNLPRSUVZYXW'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt(mess, key):
    """
    This function encrypt the message with a key
    :param mess: original message
    :param key: cipher key
    :return: encrypted message
    """
    mess = mess.upper()
    new_str = ''
    for char in mess:
        if char.isalpha():  # or can check if char.upper() in alphabet:
            index = alphabet.find(char)
            e_char = key[index]
            new_str = new_str + e_char
        else:
            new_str = new_str + char
    return new_str


print(encrypt('Hello World $*^%$*', cipher_key))


