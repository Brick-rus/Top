# ---------------------------------------------задача-----------------------------------
# Дана строка, в которой буква h встречается минимум два раза. Удалите из этой строки первое и последнее
# вхождение буквы h, а также все символы, находящиеся между ними.

# line = "qwertyhzxcvbnh123456"
# result = line[:line.find("h")] + line[line.rfind("h")+1:]
# print(result)

# ---------------------------------------------задача-----------------------------------
# Посчитайте кол-во чисел в произвольной строке (число - это набор цифр, перед числом и после числа ставятся пробелы)
# line = "qwwer 123 tyu 1245 zxc 678 qwe 123 34 fg 76 "
#
# result = line.split(" ")
# count = 0
# for i in result:
#     if i.isdigit():
#         count +=1
# print(count)

# ---------------------------------------------задача-----------------------------------
# Посчитайте кол-во букв в произвольной строке

# line = "qwwer 123 tyu 1245 zxc 678 qwe 123 asd asd345ds sdfg 76 "
#
# count = 0
# for i in line:
#     if i.isalpha():
#         count +=1
# print(count)
