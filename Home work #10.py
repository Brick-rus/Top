# -------------------------задача 1----------------------
# Найдите количество различных элементов данного массива.
# num_list = [5, 12, -2, 1.5, 24, 2, 46, 1.5, 2, 8, 3, 3, 654]
# unique_numbers = set(num_list)
#
# print(f'Длинна данного массива равна: {len(num_list)}')
# print(f'Длинна уникальных элементов массива равна: {len(unique_numbers)}')
# print(f'Уникальные элементы: {unique_numbers}')

# -------------------------задача 2----------------------
# Найти наиболее часто встречающийся элемент в массиве целых чисел.
# import random
# from collections import Counter
# num_list = []
# n = 20
# for i in range(n):
#     num_list.append(random.randint(0, 20))
# print(f'Наш список: {num_list}')
# print(f'Наше самое частое число: {Counter(num_list).most_common(1)[0][0]}')


# -------------------------задача 3----------------------
# В данном массиве найти два наименьших элемента.
#
# import random
#
# num_list = []
# n = 15
# for i in range(n):
#     num_list.append(random.randint(-50, 50))
# num_list.sort()
# print(f"Ваши два минимальных числа: {num_list[0:2]}")
# -------------------------задача 4----------------------
# Поменять местами наибольший и наименьший элементы массива

# num_list = [9, -16, 18, 14, 13, -15, 2, -10, -11, 3, -1, -7, 3, -8, 19, -12, -15, -3, 10]
# num_list.sort()
# print(num_list)  # Получили отсортированный список
# num_list[0],num_list[-1] = num_list[-1],num_list[0]  # Поменяли местами наши искомые значения
# print(num_list)


# -------------------------задача 5----------------------
# напечатать прямоугольник (заданы длина, ширина и символ) при помощи цикла for
# length, width, symbol = 6, 7, '*'
# for i in range(width):
#     print(*length * symbol)
# -------------------------задача 6----------------------
# напечатать полый прямоугольник (заданы длина, ширина и символ) при помощи цикла for
# length, width, symbol = 5, 5, '*'
# for i in range(width):
#     if i == 0 or i == (width-1):
#         print(*length * symbol)
#     else:
#         print(*symbol + ((length-2)*' ') + symbol)
