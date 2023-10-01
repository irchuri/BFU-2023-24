n = int(input("Введите количество строк треугольника Паскаля:"))
pascal = []

for stair in range(n):
    row = [1] * (stair + 1)
    for element in range(stair + 1):
        if element != 0 and element != stair:
            row[element] = pascal[stair - 1][element - 1] + pascal[stair - 1][element]

    pascal.append(row)

for stroka in pascal:
    print(stroka)


