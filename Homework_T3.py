#
# words = ' '.join(input('Введите предложение из двух слов: ').split(' ')[::-1])
# print(words, sep = ' ! ', end ='\n!!!',)


a = input('Введите ваше имя: ')
b = int(input('Укажите ваш возраст: '))
if b <= 0:
    print('повторите ввод')
elif b > 0 and b < 10:
    print('Привет шкет', a)
elif b > 10 and b <= 18:
     print('Как жизнь?', a)
elif b > 18 and b < 100:
     print('Что желаете?', a)
elif b > 100:
    print('Люди столько не живут!!!')
else:
    print('Повторите ввод')

