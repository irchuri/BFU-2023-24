# 3^k * 5^l * 7^m = x
# k l m > 0, int
# > in x
# > out 1 to x
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


x = int(input())
log1 = log(x, 3)
log2 = log(x, 5)
log3 = log(x, 7)
temp = 1
a = set()
for k in range(0, log1 + 1):
    for l in range(0, log2 + 1):
        for m in range(0, log3 + 1):
            temp = 3 ** k * 5 ** l * 7 ** m
            if temp <= x:
                a.add(temp)
b = list(a)
b.sort()
print(*b, sep=' ')


