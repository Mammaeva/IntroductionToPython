"""
Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""
import vg_functions as f

def multiplying_pairs_in_list(list: list) ->list:
    mult_pairs_list = []
    if (len(list) % 2 == 0):
        length = len(list)
    else: length = len(list)+1

    for i in range(0,int(length/2)):
        mult_pairs_list.append(list[i] * list[(len(list)) - 1 - i])

    return mult_pairs_list

num = int(input("\n Введите число длины списка: "))
list = f.rnd_int_list_n_minus_n(num)
print(f" \n Элементы списка - {num}: {list}")
mult_list = multiplying_pairs_in_list(list)
print(f" \n Список произведений пар элементов: \n{mult_list} \n")
