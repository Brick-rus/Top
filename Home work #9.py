# --------------------задача----------------------------
# # дан  список
# # запрещено использовать sort, max, map преобразовывать список в другие типы тоже нельзя
# # найти минимальный элемент в списке

# base_list = [6, 8, 4, 12, 1.5, 14, 25, 39, 241]
# num_min = base_list[0]
# for i in range(len(base_list)):
#     if num_min > base_list[i]:
#         num_min = base_list[i]
# print(f'Минимальное значение списка: {num_min}')

# --------------------задача----------------------------
# # дан  список
# # запрещено использовать sort, max, count, map преобразовывать список в другие типы тоже нельзя
# # найти элемент(ы) в списке, который повторяется дважды и более раз

# Думаю мог намудрить с решением)

# base_list = [6, 8, 4, 12, 1.5, 0, 25, 6, 241, 2, 4, 3, 3, 1.5, 3, 0]
# num = 0  # Число для последующего сравнения списка
# count = 0  # Количество вхождений
# final_list = []  # Список для проверки нахождения повторяющегося числа

# for i in range(len(base_list)):
#     num = base_list[i]
#     for j in range(len(base_list)):
#         if num == base_list[j]:
#             count += 1
#     if count > 1:
#         if num not in final_list:
#             final_list.append(num)
#     count = 0
# print(*final_list)

# --------------------задача----------------------------
# # дан список
# запрещено использовать sort, max, count, sum, map
# # сформировать новый список, с положительными числами

# from random import*
# base_list = []
# randint(-100, 100)
# n = 10
# for i in range(n):
#     base_list.append(randint(-100, 100))
# new_list = []
#
# for i in range(n):
#     if base_list[i] >= 0:
#         new_list.append(base_list[i])
# print(f'Список содержащий только положительные числа:{new_list}')


# --------------------задача----------------------------
# # дан  список
# # найти все элементы в этом списке, из которых извлекается квадратный корень в виде целого числа (4, 16 и т.д.)
# from random import*
# import math
# base_list = []
# randint(-100, 100)
# n = 10
# for i in range(n):
#     base_list.append(randint(0, 100))
#
# new_list = []
#
# for i in range(n):
#     if math.sqrt(base_list[i]) % 1 == 0:
#         new_list.append(base_list[i])
# print(f'Список с извлекаемым квадратным корнем:{new_list}')


# --------------------задача----------------------------
# # дан  список
# # найти все элементы в этом списке, у которых индекс и значение совпадают. Исходный список нельзя менять

# from random import*
#
# base_list = []
# n = 10  # Можно сделать инпутом
# randint(0, n)
# for i in range(n):
#     base_list.append(randint(0, n))
# # base_list = [6, 1, 4, 3, 8, 0, 25, 6, 8, 2, 4, 3, 12, 12, 3, 15] # как альтернатива рандомному списку
# new_list = []
# for i in range(len(base_list)):
#     if base_list[i] == i:
#         new_list.append(base_list[i])
# print(new_list)


# --------------------задача----------------------------
# # дан  список
# # запрещено использовать sort, max, count, sum, map , преобразовывать список в другие типы тоже нельзя
# # найти произведение всех элементов в этом списке
# from random import*
#
# base_list = []
# n = 10  # Можно сделать инпутом
# randint(0, n)
# for i in range(n):
#     base_list.append(randint(1, n))  # Чтобы иногда не получать 0 можно начать от 1
#
# product_of_numbers = 1
#
# for i in range(n):
#     product_of_numbers *= base_list[i]
# print(product_of_numbers)
