# ---------------------------------------задача 1---------------------------------------
# Дано число num(значение задаете сами). Напечатать “num>0”, если число больше 0, иначе - “num<0”
#
# num = int(input('Введите значение '))
# if num > 0:
#     print(f'Значение {num}>0')
# else:
#     print(f'Значение {num}<0')
# ---------------------------------------задача 2---------------------------------------
# Дано число. Напечатать, если число делится на 3, “ok”, в противном случае - ‘:(’
#
# num = int(input('Введите значение '))
# if num % 3 == 0:
#     print('ok')
# else:
#     print(':(')
# ---------------------------------------задача 3---------------------------------------
# пользователь вводит номер месяца (от 1 до 12),
# определить существует ли такой месяц (в печати указать “да” или “нет”)
# num = int(input('Введите номер месяца  '))
# if 1 <= num <= 12:
#     print('да')
# else:
#     print('нет')

# ------------------------------------Дополнительные задачи________________________________
# задача 1
# Вывести на экран число(может быть любым), если последняя цифра числа равна 8
#
# num = int(input('Введите значение '))
# if num % 10 == 8:
#     print(f'Последняя цифра числа {num} равна 8')
# else:
#     print(f'Последняя цифра числа {num} не равна 8')
# задача 2
# вывести кол-во дней в зависимости от года. Год определяет пользователь
# num = int(input('Введите год '))
# if num % 4 != 0:
#     print('365')
# elif num % 100 != 0:
#     print('366')
# elif num % 400 != 0:
#     print('365')
# else:
#     print('366')

# ---------------------------------Задача------------------------------------------
"""Пользователь вводит желаемую фигуру (“круг”, “квадрат”, “прямоугольник”, “треугольник”)
Нарисовать данную фигуру при помощи модуля turtl"""
# from turtle import *
# from time import *
# figure = input('Выберете фигуру Круг, Квадрат, Прямоугольник, Треугольник: ').lower()
#
# if figure == 'круг':
#     circle(120)
#     sleep(5)
# if figure == 'квадрат':
#     while True:
#         forward(200)
#         left(90)
#         if abs(pos()) < 1:
#             break
#     sleep(5)
# if figure == 'прямоугольник':
#     while True:
#         forward(150)
#         left(90)
#         forward(100)
#         left(90)
#         forward(150)
#         if abs(pos()) < 1:
#             break
#     sleep(5)
# if figure == 'треугольник':
#     while True:
#         forward(200)
#         left(120)
#         if abs(pos()) < 1:
#             break
#     sleep(5)
# else:
#     print('Упс... видимо где-то ошибка, попробуйте заново)')
# ---------------------------------Задача------------------------------------------
"""Пользователь выбирает хочет ли он закрасить круг или нет.
В зависимости от выбора пользователя нарисовать при помощи модуля turtle закрашенный круг или полый круг"""

# from turtle import *
# from time import *
#
# choice = input('Закрашиваем круг да или нет?: ').lower()
# if choice == 'да':
#     fillcolor('green')
#     begin_fill()
#     circle(120)
#     end_fill()
#     sleep(5)
# else:
#     circle(120)
#     sleep(5)