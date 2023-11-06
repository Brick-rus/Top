# --------------------------------------задача--------------------------------------
"""Дана произвольная строка
Написать регулярное выражение для поиска в строке серии и номера паспорта
Допускается только запись паспорта из предложенных ниже:
00 00 000000
или 00 00 000 000
или 00-00-000-000
или 00-00-000000
на месте 0 может стоять любая цифра
Программа должны вывести кол-во валидных значений и показать их в консоле"""

# import re
# input_data = '12 22 222222, 21 20 333 333, 12331323, 44-23-233-233, 20-20-145145, 12-12-45-45-45,70-20-666066, 1111 2222'
# reg_ex_1 = re.findall(r'\s*\d{2}\s\d{2}\s\d{6}',input_data)
# reg_ex_2 = re.findall(r'\s*\d{2}\s\d{2}\s\d{3}\s\d{3}', input_data)
# reg_ex_3 = re.findall(r'\s*\d{2}\-\d{2}\-\d{3}\-\d{3}', input_data)
# reg_ex_4 = re.findall(r'\s*\d{2}\-\d{2}\-\d{6}', input_data)
# print(len(reg_ex_1) + len(reg_ex_2) + len(reg_ex_3)+ len(reg_ex_4))
# print(reg_ex_1, reg_ex_2, reg_ex_3, reg_ex_4)

# ------------------------Задача----------------------------------
# написать регулярное выражение для определения номера автомобиля.
# Допускается только такая запись номера автомобиля А000АА
# А-любая буква(латиница)
# 0-любая цифра
# Программа должны вывести кол-во валидных значений и показать их в консоле

# import re
#
# input_date = "а123ух, 123ав, р1212, х071кс, М071ВД, К666СС, Т025АН"
# reg_ex = re.findall(r"\s*\w\d{3}\w{2}", input_date)
# print(len(reg_ex), reg_ex, sep='\n')

# -------------------------------Задача------------------------------
# используя модуль turtle и создав функцию рисования квадрата, решите следующую задачу:

# import turtle, time
# turtle.speed(50)
# side_of_the_square= 30  # можно сделать int(input()
#
# def square():
#     for i in range(4):
#         turtle.forward(side_of_the_square)
#         turtle.left(90)
#
# lengt = 5  # можно сделать int(input()
# width = 5  # можно сделать int(input()
# for w in range(width):
#     for l in range(lengt):
#         square()
#         turtle.penup()
#         turtle.forward(side_of_the_square)
#         turtle.pendown()
#
#     turtle.penup()
#     turtle.right(90)
#     turtle.forward(side_of_the_square)
#     turtle.right(90)
#     turtle.forward(side_of_the_square * lengt)
#     turtle.pendown()
#     turtle.right(180)
# time.sleep(5)

# ------------------------------Задача-------------------------
# создать функцию для генерации списка случайными числами

# import random
#
# number = int(input("Сколько чисел в списке?"))
# list = []
# def number_generator():
#     for i in range(number):
#         list.append(random.randint(0, 100))  # диапозон также можно задать
# number_generator()
# print(f"Ваш список: {list}")
