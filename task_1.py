#  С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

#  Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму нечётных элементов.
#  Пример:
#  - [2, 3, 5, 9, 3] ->  ответ: 20

my_list = [2, 3, 5, 9, 3]
res = sum(list(filter(lambda i:i % 2 ==1, my_list)))
print(res)

# Реализовать программу, получающую на вход строку, состоящую из слов,
# разделенных пробелами и возвращающую длину каждого слова.
# Пример: "Солнце небо воздух земля" --> 6 4 6 5

my_string = 'Я люблю семинары по Python'.split(' ')
print(my_string)
res = list(map(lambda x: len(x), my_string))
print(res)

# Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
#     Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

my_list = [1, 2, 3, 5, 1, 5, 3, 10]
new_list = []
res = list(filter(lambda x: new_list.append(x) if x not in new_list else False, my_list))
print(new_list)

# Используя параллельную итерацию сразу по двум спискам countries и capitals  выведите
# информацию о стране в формате:
# <capital> --> <country>.
# Пример:
# Москва --> Россия.

countries = ['Россия', 'США', 'Великобритания', 'Германия', 'Франция']
capitals = ['Москва', 'Вашингтон', 'Лондон', 'Берлин', 'Париж']

for country, capital in zip(countries, capitals):
    print(f'{capital} --> {country}.')

#Вывести список квадратов чисел в диапозоне от 1 до 10.

import math
list_of_squares = [math.pow(x,2) for x in range(1, 11)] # List comprehension
#list_of_squares = [x**2 for x in range(1, 11)]
print('Список квадратов:', list_of_squares)