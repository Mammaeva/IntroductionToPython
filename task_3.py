"""
Задайте последовательность чисел. Напишите программу,
которая выведет список неповторяющихся элементов исходной последовательности.
"""

import vg_functions as f

def list_unique_elements(first_list: list) ->list:
    unique_list = []
    for i in first_list:
        count = 0
        for j in first_list:
            if (j == i):
                count+=1
        if (count == 1): unique_list.append(i)
    return unique_list


num = int(input("\n Введите число уникальных элементов последовательности: "))
int_list = f.rnd_int_list_n_minus_n(num)
print(f"\n Уникальный список целых чисел:\n{int_list}")
print(f"\n Список неповторяющихся элементов исходной последовательности:")
print(f"{list_unique_elements(int_list)}\n")
