# three most popular characters

# def most_popular(stroka):
stroka = input()
spisok_char = []
spisok_cnt = []
cnt = 0
for character in stroka:
    if character not in spisok_char: spisok_char.append(character)
for i in range(0, len(spisok_char)):
    spisok_cnt.append(stroka.count(spisok_char[i]))


def cort(spisok_char, spisok_cnt):
    for i in range(0, len(spisok_cnt) - 1):
        for j in range(i + 1, len(spisok_cnt)):
            if spisok_cnt[i] < spisok_cnt[j]:
                spisok_cnt[i], spisok_cnt[j] = spisok_cnt[j], spisok_cnt[i]
                spisok_char[i], spisok_char[j] = spisok_char[j], spisok_char[i]
    return spisok_char[:3], spisok_cnt[:3]


spisok_char, spisok_cnt = cort(spisok_char, spisok_cnt)
print(f"Самые популярные символы в строке {stroka}:")
print(*spisok_char, sep='\t')
print("Их количество:")
print(*spisok_cnt, sep='\t')
