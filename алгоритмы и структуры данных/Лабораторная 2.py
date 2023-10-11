def tokenize(expression: str):
    expression_list = list()
    temp = ''
    for digit in expression:
        if digit.isdigit():
            temp += digit
        else:
            if temp != '':
                expression_list.append(temp)
            expression_list.append(digit)
            temp = ''
    if temp != '':
        expression_list.append(temp)
    if expression_list[-1] == '':
        expression_list = expression_list[:-1]
    return expression_list


def skobki(expression: list):
    while True:
        if '(' not in expression:
            break
        indeks = 0
        for i in range(len(expression) - 1, -1, -1):
            if expression[i] == '(':
                indeks = i
                break
        if expression[indeks + 1] == ')':
            raise ValueError("Проверка на дурака провалена!")
        left = expression[:indeks]
        right = expression[indeks:]
        indekss = right.index(')')
        indekss += len(left)
        right = expression[indekss + 1:]
        middle = expression[indeks:indekss + 1]
        middle = middle[1:-1]
        middle = evaluate(middle)
        expression = left + [middle] + right
    return expression


def durak(expression: list):
    stack = []
    flag = True
    t = expression
    string = ''
    for i in t:
        if i in '()':
            string += i
    for right_skobka in string:
        if right_skobka in "(":
            stack.append(right_skobka)
        elif right_skobka in ")":
            if len(stack) == 0:
                flag = False
                break

            left_skobka = stack.pop()
            if left_skobka == '(' and right_skobka == ')':
                continue
            flag = False
            break
    return not (flag == True and len(stack) == 0)


def evaluate(expression: list):
    temp = []
    for i in expression:
        if i.isdigit() or i in '*-+/':
            temp.append(i)
    expression = temp[:]

    flag = True
    while flag:
        flag = False
        for i in range(len(expression)):
            if str(expression[i]) in '*/':
                left = expression[:i - 1]
                right = expression[i + 2:]
                middle = expression[i - 1:i + 2]
                if middle[1] == "*":
                    temp = int(middle[0]) * int(middle[2])
                elif middle[1] == "/":
                    if not middle[2] == '0':
                        temp = int(middle[0]) / int(middle[2])
                    else:
                        raise ZeroDivisionError("Деление на ноль!")
                expression = left + [temp] + right
                flag = True
                break
    accum = int(expression[0])
    for i in range(1, len(expression), 2):
        if expression[i] == '+':
            accum += int(expression[i + 1])
        else:
            accum -= int(expression[i + 1])

    return str(accum)



input = input().replace(' ', '')
if not durak(input):
    print(evaluate(skobki(tokenize(input))))
else:
    print("Проверка на дурака провалена!")
