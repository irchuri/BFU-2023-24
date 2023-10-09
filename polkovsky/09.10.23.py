A = [5, 6, 3, 18, -48, 25, 6, 18]
# A.sort() - дефолт сортировка)
# адрес списка не меняется, список просто сортируется

B = sorted(A)


# создаётся новый список с новым адресом

def sumOfDigits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


A = [5, 6, 3, 18, -48, 25, 6, 18]
A.sort(key=lambda x: (sumOfDigits(x), x))
# обратный порядок:
A.sort(key=lambda x: -x)

# if key(A[1]]) > key(A[2]):
#     swap(A[1], A[2])
