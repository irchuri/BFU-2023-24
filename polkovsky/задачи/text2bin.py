'''Задание в принципе несложное. Делать его к завтрашнему дню необязательно, это как успеете.
Есть текстовый файл, в котором содержатся строки вида
название_товара цена акция
Первый элемент — str
Второй элемент — int
Третий элемент — bool
Надо прочитать оттуда всю эту информацию, записать в виде кортежей, поместить их в список,
отсортировать по названию товара в алфавитном порядке, а потом выгрузить обратно в новый
текстовый файл и новый бинарный файл (в виде байтов). Про текстовые файлы вы потом забываете,
а вот только что сформированный бинарный файл открываете на чтение, читаете из него информацию,
превращаете её обратно в кортежи, помещаете в список и сортируете его по возрастанию цены и
записываете всё в новый (уже третий по счёту) текстовый файл.'''

INPUT_FILENAME = 'input_for_sale.txt'
OUTPUT_FILENAME = 'output_for_sale.txt'
BIN_OUTPUT_FILENAME = 'bin_output_for_sale.bin'
THIRD_FILENAME = 'ya_hz_kak_eto_nazvat.txt'


def raw_to_data_format(raw_data):
    data = []
    for line in raw_data:
        # Скипаем все пустые строки
        if line == '':
            continue
        line = line.split()
        data.append(
            (
                line[0],
                int(line[1]),
                True if line[2] == 'True' else False
            )
        )
    return data


def data_to_raw_format(data):
    raw_data = []
    for line in data:
        raw_data.append(' '.join(map(str, line)))
    return '\n'.join(raw_data)


with open(INPUT_FILENAME, encoding='utf-8') as f:
    raw_data = f.read().split('\n')

data = raw_to_data_format(raw_data)
data.sort(key=lambda x: x[0])
raw_data = data_to_raw_format(data)

with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as f:
    f.write(raw_data)

with open(BIN_OUTPUT_FILENAME, mode='wb') as f:
    f.write(raw_data.encode('utf-8'))

with open(BIN_OUTPUT_FILENAME, mode='rb') as f:
    raw_data = f.read().decode('utf-8').split('\n')

data = raw_to_data_format(raw_data)
data.sort(key=lambda x: x[1])

raw_data = data_to_raw_format(data)
with open(THIRD_FILENAME, mode='w', encoding='utf-8') as f:
    f.write(raw_data)
