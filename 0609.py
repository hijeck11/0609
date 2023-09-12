str = input('введите много символов: ')
a = str[1::2]
b = str[::2]
print('введеная строка', str.strip(' '))
print(a, b, sep ='     ', end ='\n!!!')