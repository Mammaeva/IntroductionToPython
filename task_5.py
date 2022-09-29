"""
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""
def negative_fib(k: int) -> int:
    if k == -1:
        return 1
    elif k == -2:
        return -1
    else:
        return negative_fib(k + 2) - negative_fib(k + 1)

def positive_fib(k: int) -> int:
    if (k <= 1):
        return k
    else:
        return positive_fib(k - 1) + positive_fib(k - 2)

def fib_list(k: int) -> list:
    list = []

    for i in range(-k, 0):
        list.append(negative_fib(i))

    for i in range(0, k+1):
        list.append(positive_fib(i))

    return list

k = int(input(
    "\n Введите число для списка чисел Фибоначчи с + и - индексами: "))
print(f"\n Список чисел Фибоначчи для числа k = {k}:\n {fib_list(k)}\n")
