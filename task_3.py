"""
Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму
"""
def sequence_list(digit: float) -> list: #sequence - последовательность digit float - число с плавающей запятой
    list0 = []

    for i in range(1, digit+1):
        list0.append((1 + 1 / i) ** i)

    return list0

def sum_digits_list(list: list) -> float:
    sum = 0

    for i in list:
        sum += i

    return sum

n = int(input("\n Введите список из n чисел: "))
list = sequence_list(n)
sum = sum_digits_list(list)
print(f"\n Последовательность для заданного n: \n {list}")
print(f"\n Сумма элементов последовательности {n} = {round(sum,2)}\n")
