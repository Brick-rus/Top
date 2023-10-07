# -------------------задача 1----------------------
# Дана пицца 8 кусочков. Доступны команды:
# 1. print(‘Взять кусок’)
# 2. print(‘съесть кусок’)
# написать программу, симулирующую поедание кусочков пиццы

# piece = 8
# while piece != 0:
#     print("Взять кусок")
#     print(("Съесть кусок"))
#     piece -= 1

# Альтернативный способ

# piece = int(input("введите количество кусочков пиццы: "))
# for i in range(piece):
#     print("Взять кусок")
#     print(("Съесть кусок"))

# -------------------задача 2----------------------
# Выведите столбец чисел от 1 до 100, используя цикл while
# n = 1
# while n <= 100:
#     print(n)
#     n += 1
#
# -------------------задача 3----------------------
# Дано число n. Вывести степени этого числа с 1 по 10
# пример
# n=2
# 2^1=2
# 2^2=4
# …
# 2^9=512
# 2^10 = 1024

# n = int(input("Введите число: "))
# for i in range(1,11):
#     print(f"{n}^{i}={n ** i}")

# -------------------задача 4----------------------
# Написать программу для черепашки
# from turtle import *
# from time import *
# x = int(input("Введите число: "))
# shape("turtle")
# if x % 2 == 0:
#     x += 1
# for i in range(x):
#     forward(150)
#     right(180 - (360/x/2))
#     sleep(0.5
# sleep(5)

# -------------------задача 5----------------------
# Написать программу для черепашки (квадрат в квадрате)

# from turtle import *
# from time import *
# x = -10
# y = -10
#
# sq = int(input("Введите количество квадратов: "))
# length = int(input("Длина стороны: "))
# shape('turtle')
# if sq > 0 and length > 0:
#
#     for i in range(sq):
#
#         for k in range(4):
#             forward(length)
#             left(90)
#         length += 20
#         up()
#         goto(x, y)
#         x -= 10
#         y -= 10
#         down()
# else:
#     print("Упс... Какое-то из значений меньше или равно нули, попробуйте другие значения ")


# ---------------------------- Задача -----------------------
"""Выведите столбец чисел от start (определяется пользователем) до end,
используя цикл while. Найти произведение чисел"""
### Вопрос к ТЗ. Программа выполняет выдачу чисел от start до end и выдает произведение,
### без оговорок на отрицательные числа.
# start = int(input("Введите число: "))
# end = int(input("Введите число: "))
# result = 1
# if start < end:
#     while start <= end:
#         print(start)
#         result *= start
#         start += 1
#     print(result)
# else:
#     while start >= end:
#         print(start)
#         result *= start
#         start -= 1
#     print(result)
