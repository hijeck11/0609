str = input('введите много символов: ')
a = str[1::2]
#print('введеная строка', str.strip(' '))
print('введеная строка', a, b, sep ='     ', end ='\n!!!')
#
#
# name = "Pavel"
# "hello {var}".format(var=name)
#
# print(name)
#


# [spam, ham] = ['yam', 'nym']
# print(spam)
# print(ham)

# a, *b = 'spam'
# print(a)
# print(b)

# spam += 42
# print(spam)

# firstname = input('input your first name: ')
# lastname = input('input your last name: ')
#
# string_a = 'Hello, %s%s'%(firstname, lastname)
# string_b = 'Hello, {}{}'.format(firstname, lastname)
# string_c = 'Hello, {0}{1}'.format(firstname, lastname)
# string_d = f'Hello, {firstname}{lastname}'
# c = 'Hello'

# ab = input(str("Введите предложение из двух слов: "))
# a = input(str('Введите первое слово: '))
# b = input(str('Введите второе слово: '))
# a, b = b, a
# print(a, b, sep= '! !', end= '!')

#
# def add(a, b):
#     return a / b
# print(add(1, 22))


# def sum(a, b):
#     return a+b
# print(sum(15,5))


# def summ_1(a, b):
#     print(a, b)
#     return a+b
#
# def summ2():
#     print('Набор функции')
#     x = summ_1(5,5)
#     print(x + 5)
#
# summ2()

# def full_func(*args, **kwargs):
#     print(args)
#     print(kwargs)
# full_func(1,2,3,a=4,b=5,c=6)

# def my_func(**kwargs):
#     keys, values = [], []
#     for key, value in kwargs.items():
#         print(key, value)
#         keys.append(key)
#         values.append(value)
#     return keys, values
# keys, values = my_func(a=5)

# x = 10
# def func():
#     global x
#     print(x)
#     x = 20
#     print(x)
#
# func()

# random_list = [i for i in range(1,15)]
# print(random_list)