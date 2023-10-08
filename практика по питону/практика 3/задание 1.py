# YYYYggkeeeAAABV -> Y4g2ke3A3BV

def cipher(stroka):
    cur_chr = stroka[0]
    cipher_str = ''
    count = 1
    for i in range(1, len(stroka)):
        if stroka[i] == cur_chr:
            count += 1
        else:
            cipher_str += cur_chr + str(count)
            cur_chr = stroka[i]
            count = 1

    cipher_str = cipher_str.replace('1','')
    return cipher_str




stroka = input("Введите строку, которую нужно зашифровать:")
print(cipher(stroka))