"""
№1. Создайте родительский класс auto, у которого есть атрибуты: brand, age, color, mark and weight. А так же методы; move, birthday и stopю Методы move и stop выводят сообщение на экран....
"""
class auto:
    def __init__(self, brand, age, color, mark, weight):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        print(self.age + 1)

car1 = auto('zaz', 30, 'red', '968', 1000)
car1.birthday()
