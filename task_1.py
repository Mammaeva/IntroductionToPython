"""
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""

import vg_functions as f

def odd_position_in_list(pos: list) -> list:
    odd_pos = []

    for i in range(1, len(pos), 2):
        odd_pos.append(pos[i])

    return odd_pos

num = int(input("\n Введите число длины списка: "))
pos = f.rnd_int_list_n_minus_n(num)
print(f'\n Элементы списка - {num}:\n{pos}')
odd_pos = odd_position_in_list(pos)
print(f'\n Элементы списка с нечетными индексами:\n{odd_pos}')
sum = f.sum_indices_list(odd_pos)
print(f'\n Cумма элементов списка нечетных позиций: {sum}\n')
