# -----------------------Задача №1-------------------------------
# Пользователь вводит сумму вклада в банк и годовой процент. Найдите сумму вклада через 5 лет

# amount = int(input('Введите сумму которую хотите положить на вклад в банк  '))
# percent = float(input('Введите процент вклада  '))
# years = 5
# total = ((amount * percent / 100) * 5) + amount
# print(f' Ваша сумма через {years} лет составит {total}')


# -----------------------Задача №2-------------------------------
# Дано значение температуры в градусах Цельсия. Вывести температуру  в градусах Фаренгейта.
# cel = float(input('Введите температуру в цельсиях '))
# far = float(cel * 9 / 5 + 32)
# print (f'Температура в Фаренгейтах равна {far}')

# -----------------------Задача №3-------------------------------
""" Пользователь вводит количество дней, указывает процент скидки и вводит сумму.
<<<<<<< HEAD
 Рассчитать итоговую сумму, если за каждый день сумма увеличивается на 3 $ и затем применяется скидка,
=======
 Рассчитать итоговую сумму, если за каждый день сумма увеличивается на 3 $  и затем применяется скидка,
>>>>>>> origin/master
 то есть итоговая сумма еще уменьшится на данное число процентов. """

# day = int(input('Введите количество дней '))
# sell = int(input('Введите скидку '))
# summ = int(input('Введите сумму '))
# total = (day * 3 + summ) * sell / 100 + summ
# print(f'Итоговая сумма равна {total}')

# -----------------------Задача №4-------------------------------
"""Из трехзначного числа x вычли его последнюю цифру. 
Когда результат разделили на 10, а к частному слева приписали последнюю цифру числа x,
то получилось число 237. Найти число x."""

# x = int(input('Введите трехзначное число '))
# last_number = x % 10
# result = x - last_number
# z = int(result / 10)
# print(last_number, z, sep='')


# -----------------------Задача №5-------------------------------
# Дано трехзначное число. Найти произведение цифр
# # пример 123 1*2*3=6
# x = int(input('Введите трехзначное число '))
# result = (x // 100) * (x % 100 // 10) * (x % 10)
# print(f'Произведение трехзначного числа равно {result}')

# -----------------------Задача №6-------------------------------
<<<<<<< HEAD
# Поменяйте местами значения двух переменных, не используя дополнительных переменных.
=======
#Поменяйте местами значения двух переменных, не используя дополнительных переменных.
>>>>>>> origin/master

# x, y = int(input('Введите значение для х ')), int(input('Введите значение для у '))
# x, y = y, x
# print(f' Теперь значение х равно {x}, а  значение у равно {y}')

<<<<<<< HEAD
# ------------------Усложнённые задачи---------------------------------
=======
# ------------------Усложненые задачи---------------------------------
>>>>>>> origin/master
# x = int(input('Введите число '))
# result = list(set(map(int, str(x))))
# summ = 1
# for x in result:
#         summ = summ * x
# print(summ)
#
# # -------------------------------------------------------------------------
# x = int(input('Введите число '))
# result = list(set(map(int, str(x))))
# result.sort()
# print(result[-2])
