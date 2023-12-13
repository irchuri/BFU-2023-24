import csv


def Show(csvfile, parameter="top", quantity=5, separator=","):
    with open(csvfile, 'r', encoding="utf-8") as file:
        reader = list(csv.reader(file))
        header = reader.pop(0)
        print(f'{separator} '.join(header))

        if quantity > len(reader):

            if parameter == "top":
                for row in reader:
                    print(f'{separator} '.join(row))

            elif parameter == "bottom":
                for row in reversed(reader):
                    print(f'{separator} '.join(row))

            elif parameter == "random":
                import random
                random_list = reader
                random.shuffle(random_list)
                for row in random_list:
                    print(f'{separator} '.join(row))
            print("Указано недостаточное количество строк :(")
            print(len(reader))

        else:
            i = 0
            if parameter == "top":
                for row in reader:
                    print(f'{separator} '.join(row))
                    i += 1
                    if i == quantity:
                        break

            elif parameter == "bottom":
                for row in reversed(reader):
                    print(f'{separator} '.join(row))
                    i += 1
                    if i == quantity:
                        break

            elif parameter == "random":
                import random
                for row in random.sample(reader, quantity):
                    print(f'{separator} '.join(row))
                    i += 1
                    if i == quantity:
                        break
            else:
                print(f'Параметр {parameter} не распознан')


def Info(csvfile):
    with open(csvfile, 'r', encoding="utf-8") as file:
        rows = list(csv.reader(file))
        header = rows.pop(0)
        non_empty_rows = list(x for x in rows if x != [])
        count_of_non_empty_rows = len(non_empty_rows)
        print("Количество строк с данными на количество столбцов:")
        print(f"{count_of_non_empty_rows}x{len(header)}")
        for i in range(len(header)):
            count_of_columns_with_data = sum(
                1 for x in non_empty_rows if x[i].replace(
                    " ", ""
                ) != ""
            )
            h = header[i].replace(" ", "")
            t = get_type_of_var(non_empty_rows[0][i])
            print(f"{h} {count_of_columns_with_data} {t}")


def get_type_of_var(var) -> str:
    result = ""
    try:
        int(var)
        result = "int"
    except ValueError:
        try:
            float(var)
            result = "float"
        except ValueError:
            str(var)
            result = "string"
    return result


def DelNaN(csvfile):
    with open(csvfile, "r") as file:
        rows = list(csv.reader(file))
        deleted_rows = []
        for row in rows:
            for column in row:
                if column.replace(" ", "") == "":
                    print(f"Обнаружена строка с пустым полем {row}")
                    deleted_rows.append(row)
                    break

        for del_row in deleted_rows:
            rows.remove(del_row)

        result = open("new_data.csv", "w")
        res_writer = csv.writer(result)
        for row in rows:
            res_writer.writerow(row)
        result.close()


def MakeDS(csvfile):
    import random
    import os

    with open(csvfile, "r") as file:
        rows = list(csv.reader(file))
        header = rows.pop(0)
        len_rows = len(rows)
        random.shuffle(rows)
        seventy_percent_rows = round(len_rows / 100 * 70)
        thirty_percent = len_rows - seventy_percent_rows

        try:
            train = open("final_1_stage/workdata/learning/train.csv", "w")
        except FileNotFoundError:
            if not os.path.exists("final_1_stage/workdata/learning"):
                os.mkdir("final_1_stage/workdata/learning")
            train = open("final_1_stage/workdata/learning/train.csv", "w")
        train_writer = csv.writer(train)
        train_writer.writerow(header)
        print(header)
        for i in range(seventy_percent_rows):
            print(rows[i])
            train_writer.writerow(rows[i])
        train.close()

        try:
            test = open("final_1_stage/workdata/testing/test.csv", "w")
        except FileNotFoundError:
            if not os.path.exists("final_1_stage/workdata/testing"):
                os.mkdir("final_1_stage/workdata/testing")
            test = open("final_1_stage/workdata/testing/test.csv", "w")
        test_writer = csv.writer(test)
        test_writer.writerow(header)
        print(header)
        for i in range(thirty_percent):
            print(rows[seventy_percent_rows + i])
            test_writer.writerow(rows[seventy_percent_rows + i])
        test.close()


path_to_csvfile = "data.csv"
Show(path_to_csvfile, parameter="random", quantity=5, separator=",")
Info(path_to_csvfile)
DelNaN(path_to_csvfile)
MakeDS(path_to_csvfile)
