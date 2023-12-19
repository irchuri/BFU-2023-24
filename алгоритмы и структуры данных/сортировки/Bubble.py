spisok = list(map(int, input().split()))
flag = True

while flag:
    flag = False
    for i in range(0, len(spisok) - 1):
        if spisok[i] > spisok[i + 1]:
            spisok[i], spisok[i + 1] = spisok[i + 1], spisok[i]
            flag = True
print(*spisok, sep=' ')
