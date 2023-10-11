
#Калькулятор c применением try/except и своим исключением
class Error(Exception):
    def __str__(self):
        return 'Введен не допустимый символ'
    def calcul(self, b):
        symbols = ['+', '-', '/', '*']
        if c not in symbols:
            raise Error ('Вы ввели неккоректный оператор вычисления')


try:
    a = float(input("Введите первое число = "))
    c = input('Выберите знак +, -, *, /: ')
    b = float(input("Введите второе число = "))
    e = Error()
    e.calcul(c)
    result = 0
    if c == "+":
        res = a + b
        print('Ваш результат: ', res)
    elif c == "-":
        res = a - b
        print('Ваш результат: ', res)
    elif c == "*":
        res = a * b
        print('Ваш результат: ', res)
    elif c == "/":
        res = a / b
        print('Ваш результат: ', res)

except ZeroDivisionError:
    print('Делить на ноль нельзя')
except ValueError:
    print('Скорее всего вы вводите буквы')
except Error:
    print('Вы ввели неккоректный оператор вычисления')
#
