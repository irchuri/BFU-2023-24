''' По теории игр надо написать программу,
которая в цикле предлагает пользователю сделать на выбор один из двух ходов:
первый ход как-либо увеличивает количество камней в куче,
а второй каким-либо образом уменьшает. Число, на которое увеличивается или уменьшается количество камней,
всякий раз меняется и выбирается случайным образом.
Выигрыш происходит тогда, когда пользователю удаётся довести количество камней в куче до нуля.
При этом количество камней может стать отрицательным, и игра на этом не заканчивается.'''


import random
N = 10
MIN = 0
MAX = 10
if MIN < 0:
    raise ValueError('Минимальный шаг не может быть меньше 0')
if MAX <= MIN:
    raise ValueError('Максимальный шаг не может быть меньше минимального')

steps = 0
while N != 0:
    print(f'\nШаг {steps + 1}')
    while True:
        print(f'Количество камней: {N}')
        user_choice = input('Уменьшить (-) или увеличить(+)?: ')
        if user_choice in ['+', '-']: break
    step = random.randint(MIN, MAX)
    step = user_choice + str(step)
    print(step)
    N += int(step)
    steps += 1
print(f'\nПобеда за {steps} ходов!')
