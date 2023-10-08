# Y4g2ke3A3BV -> YYYYggkeeeAAABV
# list of lists (letter, count)

def create_pairs(stroka):
    pairs = []
    cur_char = None
    cur_dig = 0
    for character in stroka:
        if character.isalpha():
            if cur_char is not None:
                pairs.append([cur_char, cur_dig])
            cur_char = character
            cur_dig = 1
        elif character.isdigit():
            cur_dig += int(character) - 1
    if cur_char is not None:
        pairs.append([cur_char, cur_dig])

    return pairs


stroka = input("Введите строку для дешифровки:")
new_stroka = ''
pairs = create_pairs(stroka)
for element in pairs:
    new_stroka += element[0] * element[1]
print(new_stroka)
