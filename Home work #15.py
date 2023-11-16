# --------------------------------------задача--------------------------------
#Дана произвольная строка создать строку, в которой содержаться только цифры из исходной строки
# ПРимер
# ввод
# АА”АА324А К*К№5 10 79
# # вывод
# 32451079

# def search_for_numbers(input_data):
#     result = []
#     for i in range(len(input_data)):
#         if input_data[i].isdigit() == True:
#             result.append(input_data[i])
#     print(*result, sep='')  # Если надо с пробелами, то можем убрать sep
#
#
# input_data = "Аdf1А”А2А324А К*К№5 10 79"
# search_for_numbers(input_data)
# input_data = "hell23avro34run4,.03da"
# search_for_numbers(input_data)

# --------------------------Задача--------------------------------
# Дан список чисел (можно создать любым способом, но приветствуется через лямбду функцию и random).
# Необходимо создать новый список чисел, которые будут составлять 70% от исходного числа.
# Для создания такого списка использовать функцию map().
# Необходимо посчитать разницу между суммами исходного списка и преобразованного
# ПРИМЕР
# ввод
# 100, 50, 30 (сумма 180)
# 70, 35, 21 (сумма 126)
# вывод
# 54

# import random
#
# list_1 = [random.randint(1, 100) for i in range(10)]
# list_07 = list(map(lambda num: int(num * 0.7), list_1))
# print(f'Список исходный :{list_1} и его сумма {sum(list_1)},'
#       f'\nСписок полученный {list(list_07)} и его сумма {sum(list_07)}')
# result = sum(list_1)-sum(list_07)
# print(f'Разность между списками равна:{result}')


# ---------------------Задача -------------------------------
# Дана строка, состоящая из символов X, Y, и Z.
# Определите максимальное количество идущих подряд символов, среди которых нет подстроки XZZY.

# string = "XZZYXXZZYZXYYZXYZXZZYYXZXZXYXYYXYZYXXZXZZYXZXZXYZZZYXYYZXCZXYZXZXYZXYZXZXXYYXZZYZXYYZX"
#
# resulting_string = lambda x: x.split("XZZY")
# result = len(max(resulting_string(string), key=len))
# print(result)