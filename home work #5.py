# ---------------------------ЗАДАЧА 1--------------------------------------
# Дано:
# 3 стороны треугольника
# Проверить существует ли треугольник.
# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.

# x = int(input("Введите первую сторону: "))
# y = int(input("Введите вторую сторону: "))
# z = int(input("Введите третью сторону: "))
# if x + y > z and x + z > y and z + y > x:
#     print("Треугольник существует")
# else:
#     print("Треугольник не существует")


# ---------------------------ЗАДАЧА 2--------------------------------------
# Дано:
# из чего переводим: часов, минут, секунд (что-то одно на выбор пользователя)
# во что переводим: часов, минут, секунд (что-то одно на выбор пользователя)
# кол-во переводимых единиц
#
# реализовать интерфейс для перевода из (часов, минут, секунд) в (часов, минут, секунд)

# it_was = input("Будем переводить из часов, минут или секунд: ").lower()
# it_became = input("Будем переводить в часы, минуты или секунды: ").lower()
# data = ["час", "часы", "часов", "минута", "минут", "минуты", "секунда", "секунд", "секунды"]
# count = int(input("Укажите количество: "))
# hour = ["час","часы", "часов"]
# minutes = ["минута", "минут", "минуты"]
# seconds = ["секунда", "секунд", "секунды"]
#
# if it_was in data and it_became in data and count > 0:
#     if it_was in hour and it_became in minutes:
#         print(f'Переводим {count} часов в минуты: {count * 60}')
#     elif it_was in hour and it_became in seconds:
#         print(f'Переводим {count} часов в секунды: {count * 3600}')
#     elif it_was in minutes and it_became in seconds:
#         print(f'Переводим {count} минут в секунды: {count * 60}')
#     elif it_was in minutes and it_became in hour:
#         print(f'Переводим {count} минут в часы: {count / 60}')
#     elif it_was in seconds and it_became in minutes:
#         print(f'Переводим {count} секунд в минуты: {round(count / 60, 2)}')
#     elif it_was in seconds and it_became  in hour:
#         print(f'Переводим {count} секунд в часы: {round(count / 3600, 2)}')
# else:
#     print("Вы где то совершили ошибку, попробуйте заново.")

# ---------------Альтернативный способ решения задачи---------------------
# it_was = input("""
# Выберите систему перевода
#     1 - Из часов
#     2 - Из минут
#     3 - из секунд """)
# it_became = input("""
# Выберите систему перевода
#     1 - В часы
#     2 - В минуты
#     3 - В секунды""")
# count = int(input("Укажите количество: "))
# result = it_was + it_became
# combinations = ["12", "13","21", "23", "31", "32"]
# if count > 0 and result in combinations:
#     match result:
#         case '12':
#             print(f"Переводим в минуты: {count * 60}")
#         case '13':
#             print(f"Переводим в секунды: {count * 3600}")
#         case '21':
#             print(f"Переводим в часы: {round(count / 60, 2)}")
#         case '23':
#             print(f"Переводим в сеекунды: {count * 60}")
#         case '31':
#             print(f"Переводим в часы: {count / 3600}")
#         case '32':
#             print(f"Переводим в минуты: {count / 60}")
# else:
#     print("Вы где то совершили ошибку, попробуйте заново.")


# -------------------------ЗАДАЧА 3 ПОИСК ОШИБОК-----------------------------#
# калькулятор
# доступны операции умножить и поделить
# ------ДО-----
# num1 = 5
# operation = '*'
# num2 = 6
# if operation == '*':
#     print(num1/num2)
# if operation == '/':
#     print(num1/num2)
# else:
#     print("нет такой операции")

# ------После-----
# num1 = int(input("Выберете первое число "))  # Лучше конечно добавить int(input()) или float(input())
# num2 = int(input("Выберете второе число "))  # Лучше конечно добавить int(input()) или float(input())
# operation = input("Выберете оператора +, -, *, /")  # Операцию лучше перенести после ввода
# # данных и дать пользователю выбор input()
#
# if operation == '*':
#     print(num1 * num2)  # Необходимо заменить операцию на которую указано в дано
# elif operation == '/' :
#     if num1 == 0 or num2 == 0:  # Добавляем проверку, что одно из чисел не равно нулю
#         print('Делить на ноль нельзя')
#     else:  # Иначе проводи деление
#         print(round(num1/num2, 2))  # Можно добавить округление до двух знаков после запятой
# elif operation == '+':  # Добавляем оставшиеся операторы
#     print(num1 + num2)
# elif operation == '-':  #Добавляем оставшиеся операторы
#     print(num1 - num2)
# else:
#     print("Нет такой операции")


# --------------------------------------------------ЗАДАЧА-----------------------------------------------
"""Топливо и черепаха
черепахе выдается какое-то кол-во чернил, а также фигуру, которая она должна нарисовать (круг или квадрат),
а также площадь фигуры Определите, хватит ли черепахе чернил
Если чернил не хватает, попросите пользователя дозаправить ее чернила"""

# import math
# fuel = int(input("Введите количества топлива: "))
# figure = int(input("""Что будем рисовать:
# Если квадрат нажми 1
# Если круг нажми 2
#                 """))
#
# if figure <= 2 and figure >= 1:
#     square = int(input('А теперь введите площадь фигуры: '))
#     if figure == 1:
#         side_square = math.sqrt(square)
#         if fuel >= side_square:
#             print("Топлива хватит для изображения квадрата")
#         else:
#             print(f"Чернил не хватит, необходимо дозаправить черепаху на {side_square-fuel} единиц")
#     if figure == 2:
#         circle = round(math.sqrt(4 * square * math.pi), 2)
#         if fuel >= circle:
#             print("Топлива хватит для изображения квадрата")
#         else:
#             print(f"Чернил не хватит, необходимо дозаправить черепаху на {round(circle-fuel, 2)} единиц")
# else:
#     print("Можно выбрать только 1 или 2")

# ------------------------ЗАДАЧА----------------------------------
# Дано
# * кол-во цифр в пароле (не делать проверку на отрицательность)
# * кол-во малых букв в пароле (не делать проверку на отрицательность)
# * кол-во заглавных букв в пароле (не делать проверку на отрицательность)
# * кол-во запрещенных символов в пароле (не делать проверку на отрицательность)
# Для использования пароля необходимо:
# * минимум 1 цифру, 1 малую букву, 1 заглавную букву
# * в пароле не должно быть запрещенных символов
# * минимальная длина пароля 6 символов
# Написать можно ли использовать такой пароль
### Надеюсь я правильно понял ТЗ

# numbers = input('Цифры: ')
# lower_letters = input('Прописные буквы: ').lower()
# uppercase_letters = input('Заглавные буквы: ').upper()
# forbidden_characters = input('Символы: ')
# password = numbers + lower_letters + uppercase_letters
# if len(numbers) >= 1 and len(lower_letters) >= 1 and len(uppercase_letters) >= 1 and len(forbidden_characters) == 0 and len(password) >= 6:
#     print('Пароль с такими данными можно использовать')
# else:
#     print('Пароль нельзя использовать')
