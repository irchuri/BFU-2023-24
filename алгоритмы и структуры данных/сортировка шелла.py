from random import randint


def log(num, base):
    cnt = 0
    temp1 = base
    while temp1 < num:
        cnt += 1
        temp1 = base ** cnt
    if temp1 == num:
        return cnt
    else:
        return cnt - 1


spisok = [randint(-100, 100) for i in range(20)]
# spisok = list(map(int, input().split()))

print(spisok)

n = len(spisok)
k = int(log(n, 2))
shag = 2 ** k - 1
while shag > 0:
    for i in range(shag, n):
        temp = spisok[i]
        j = shag
        while j >= shag and spisok[j - shag] > temp:
            spisok[j] = spisok[j - shag]
            j -= shag
        spisok[j] = temp
    k -= 1
    shag = 2 ** k - 1
print(spisok)
