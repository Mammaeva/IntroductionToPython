"""
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
"""

def recursion(num):  # рекурсия
    if num == 1:
        return ''
    i = 2
    while True:
        if num % i == 0:
            break
        i+=1
    return str(i) + " " + recursion(int(num/i))
num = int(input("Введите число N = "))
print(recursion(num))
