import re
alice_dict = {}
with open('alice.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = re.sub('[^a-zA-Z0-9 \-]', '', line).lower()
        # word_list = line.split()
        word_list = re.split('[\s_\-]+', line)
        for word in word_list:
            if word != '':
                if word in alice_dict:
                    alice_dict[word] += 1
                else:
                    alice_dict[word] = 1
alice_dict = dict(sorted(alice_dict.items(), key=lambda x: x[0]))
max_len = 0
max_len_w = ''
for key in alice_dict:
    if len(key) > max_len:
        max_len = len(key)
        max_len_w = key
print('Longest word:', max_len_w, 'with len:', max_len)
print(alice_dict['id'])
print(alice_dict)
