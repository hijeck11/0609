"""
1. Создайте свой класс данных
2. Добавить в класс статикметод
3. Добавить в класс классметод
4. Создать метокласс
"""

class Temp:
    def __init__(self):
        MIN_temp = 0
        MAX_temp = 100

    @classmethod
    def avg_temp(cls, arg):
        return cls.MIN_temp <= arg <= cls.MAX_temp

print(Temp.avg_temp(15))