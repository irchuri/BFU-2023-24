numbers9 = {1: "один",
            2: "два",
            3: "три",
            4: "четыре",
            5: "пять",
            6: "шесть",
            7: "семь",
            8: "восемь",
            9: "девять"}
numbers11 = {0: "десять",
             1: "одиннадцать",
             2: "двенадцать",
             3: "тринадцать",
             4: "четырнадцать",
             5: "пятнадцать",
             6: "шестнадцать",
             7: "семнадцать",
             8: "восемнадцать",
             9: "девятнадцать"}
numbers10 = {2: "двадцать",
             3: "тридцать",
             4: "сорок",
             5: "пятьдесят",
             6: "шестьдесят",
             7: "семьдесят",
             8: "восемьдесят",
             9: "девяносто"}
numbers100 = {1: "сто",
              2: "двести",
              3: "триста",
              4: "четыреста",
              5: "пятьсот",
              6: "шестьсот",
              7: "семьсот",
              8: "восемьсот",
              9: "девятьсот"}


stroka = (input("Введите число:"))
if not stroka.isdigit():
    print("Введённая строка не является числом :(")
    exit(0)

stroka = list(stroka)
stroka = list(map(int, stroka))
# print(stroka)
if len(stroka) == 1:
    print(numbers9[stroka[0]])
elif len(stroka) == 2:
    if stroka[0] == 1:
        print(numbers11[stroka[1]])
    else:
        print(numbers10[stroka[0]], numbers9[stroka[1]])
elif len(stroka) == 3:
    print(numbers100[stroka[0]], end=' ')
    if stroka[1] == 0:
        if stroka[2] != 0:
            print(numbers9[stroka[2]])
        else:
            exit(0)
    elif stroka[1] == 1:
        print(numbers11[stroka[1]])
    else:
        print(numbers10[stroka[1]], numbers9[stroka[2]])
