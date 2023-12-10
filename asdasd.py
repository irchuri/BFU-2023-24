def isPrime(x):
    if x == 1:
        return False
    else:
        flag = True
        for i in range(2, x):
            if x % i == 0:
                flag = False
                break
    if flag:
        return "prime"
    else:
        return "primen't"


print(isPrime(int(input())))
