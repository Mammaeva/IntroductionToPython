"""
Задайте список из вещественных чисел. Напишите программу,
которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""
import vg_functions as f

def fractional_part_in_list(list: list) -> float:
    fract_list = []

    for elements in list:
        fract_elem = False
        fract_element = "0."

        for j in range(0, len(str(elements))):
            if fract_elem:
                fract_element += str(elements)[j]
            if not fract_elem and (str(elements)[j] == "."):
                fract_elem = True

        fract_list.append(float(fract_element))

    min_float = fract_list[0]
    max_float = fract_list[0]

    for f in fract_list:
        if f < min_float:
            min_float = f
        if f > max_float:
            max_float = f

    solution = round((max_float - min_float), 2)
    return solution

num = int(
    input("\n Введите число длины списка: "))
list = f.rnd_float_list_n_minus_n(num)
print(f"\n Cписок из {num} элементов: {list}")
solution = fractional_part_in_list(list)
print(f"\n Разница между макс-ым и миним-ым значением дробной части элементов: {solution}\n")
