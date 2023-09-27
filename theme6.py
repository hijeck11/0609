# #1. Декодировать в строку байтовое значение
# a = b'r\xc3\xa9sum\xc3\xa9'
# b = a.decode('UTF-8')
# print(b)
# c = b.encode('Latin 1')
# e = c.decode('UTF-8')
# print(e)
#
# # 2 ввести 4 строки, записать первые две, каждую новой строкой, закрыть файл, открыть на дозапись и дозаисать 3 и 4 строки.
#
# # f = open('D:\TMS\homework\homework\test.txt, 'r')
# # print(f.read())
# str_1 = str(input('Введите строку_1: '))
# str_2 = str(input('Введите строку_2: '))
# str_3 = str_1, str_2
# str_4 = str(input('Введите строку_3: '))
# str_5 = str(input('Введите строку_4 '))
# str_6 = str_4, str_5
# f = open(r'D:\TMS\homework\homework\test.txt', 'w')
# for line in str_3:
#     f.write(line + '\n')
# f.close()
# f = open(r'D:\TMS\homework\homework\test.txt', 'a')
# for line in str_6:
#     f.write(line + '\n')
# f.close()

# #3 Создать словарь в качестве ключа которого будет 6-ти значный id, а в качестве значвений кортеж состояжий из двух элементов имя(str), возраст(int). Сделать около 5-6 элементов словаря. Записать данные словаря на диск в json-файле.

import json

family = {
    111111: ('Pap', 30),
    222222: ('Mom', 27),
    333333: ('Dot', 5),
    444444: ('Sun', 4),
    555555: ('Bro2', 35),
}
family_json = json.dumps(family)
with open("data_file.json", "w") as f:
    f.write(family_json)