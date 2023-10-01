
string = input("Введите строку:")
stack = []
flag = True

for right_skobka in string:
    if right_skobka in "({[":
        stack.append(right_skobka)
    elif right_skobka in ")}]":
        if len(stack) == 0:
            flag = False
            break

        left_skobka = stack.pop()
        if left_skobka == '(' and right_skobka == ')':
            continue
        if left_skobka == '{' and right_skobka == '}':
            continue
        if left_skobka == '[' and right_skobka == ']':
            continue

        flag = False
        break

if flag == True and len(stack) == 0:
    print("Строка хорошая)")
else:
    print("Строка нехорошая(")

print("гит говно")