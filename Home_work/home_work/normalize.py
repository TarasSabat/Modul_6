import re

CYRILLIC_SYMBOLS = 'абвгдежзйклмнопрстуфхцчшщюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "j", "z", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "yu", "ja", "je", 'i', "ji", "g")

TRANS = dict()

for cyrillic, latin in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(cyrillic)] = latin
    TRANS[ord(cyrillic.upper())] = latin.upper()


def normalize(name: str) -> str:
    translate_name = name.split('.')
    translate_name[0] = re.sub(r'\W', '_', translate_name[0].translate(TRANS))
    my_name = ('.'.join(translate_name))
    return my_name


