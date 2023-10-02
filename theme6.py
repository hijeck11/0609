# todo №1. Декодировать в строку байтовое значение
# a = b'r\xc3\xa9sum\xc3\xa9'
# b = a.decode('UTF-8')
# print(b)
# c = b.encode('Latin 1')
# e = c.decode('UTF-8')
# print(e)
#
# todo №2. Ввести 4 строки, записать первые две, каждую новой строкой, закрыть файл, открыть на дозапись и дозаисать 3 и 4 строки.
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

# todo №3. Создать словарь в качестве ключа которого будет 6-ти значный id,
# а в качестве значвений кортеж состояжий из двух элементов имя(str),
# возраст(int). Сделать около 5-6 элементов словаря.
# Записать данные словаря на диск в json-файле.

# import json
# # # #
# family = {
#     111111: ('Pap', 30),
#     222222: ('Mom', 27),
#     333333: ('Dot', 5),
#     444444: ('Sun', 4),
#     555555: ('Bro2', 35),
# }
# family_json = json.dumps(family)
# with open("data_file.json", "w") as f:
#     f.write(family_json)

# todo №4. Прочитать данный JSON и записать данные на диск в CSV файл. делаем импорт из json в CSV попутно редактируя

# import csv
# import json
#
# # Загрузить данные из JSON-файла
# with open("data_file.json", "r") as f:
#     family_json = f.read()
#     family = json.loads(family_json)
#
# # Открыть файл CSV для записи
# with open("data_file.csv", "w", newline="") as csvfile:
#     csv_writer = csv.writer(csvfile)
#
#     # Записать заголовок (заголовок CSV)
#     csv_writer.writerow(["ID", "Name", "Age"])
#
#     # Записать данные из словаря в CSV
#     for key, (name, age) in family.items():
#         csv_writer.writerow([key, name, age])
#
# import pandas as pd

# Чтение CSV-файла
# df = pd.read_csv("data_file.csv")
#
# # Создание столбца "телефон" с данными
# df["телефон"] = ["+1234567890", "+9876543210", "+5555555555", "+1111111111", "+9999999999"]
#
# # Сохранение обновленного CSV-файла
# df.to_csv("data_file.csv", index=False)
#
# print("Столбец 'телефон' успешно добавлен в файл data_file.csv.")

# todo прочитать данный CSV-файл и сохранить его в exel-файл. Попутно удалить столбец "возраст".
# Сразу удалим ненужный столбец "возраст"
# import pandas as pd
#
# # Загрузите CSV-файл
# df = pd.read_csv("data_file.csv")
#
# # Удалите столбец "возраст"
# df = df.drop("Age", axis=1)
#
# # Сохраните обновленный DataFrame обратно в CSV-файл
# df.to_csv("data_file2.csv", index=False)

# import pandas as pd
#
# # Загрузите CSV-файл
# df = pd.read_csv("data_file2.csv")
#
# # Сохраните данные в формате Excel (.xlsx)
# df.to_excel("data_file.xlsx", index=False)