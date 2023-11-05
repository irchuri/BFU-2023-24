from random import randint

def log(num, base):
    cnt = 0
    temp = base
    while temp < num:
        cnt += 1
        temp = base**cnt
    if temp == num:
        return cnt
    else:
        return cnt-1


spisok = [randint(-100, 100) for i in range(10)]
#spisok = list(map(int, input().split()))

print(spisok)

n = len(spisok)
k = int(log(n,2))
interval = 2**k -1
while interval > 0:
    for i in range(interval, n):
        temp = spisok[i]
        j = i
        while j >= interval and spisok[j - interval] > temp:
            spisok[j] = spisok[j - interval]
            j -= interval
        spisok[j] = temp
    k -= 1
    interval = 2**k -1
print(spisok)
