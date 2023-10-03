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

"""
№2 Создать 2 класса truck и car, которые являются наследниками класса auto. Класс truck имеет допонительный .....
"""
class truck(auto):
    def __init__(self, max_load):
        self.max_load = max_load

    def move(self):
        print('attention')
        super().move()

    def load(self):
        import time
        pause = time.sleep(1)
        print('load')
        pause = time.sleep(1)

class car(auto):
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def move(self):
        super().move()
        print('max speed is:', self.max_speed)

MAN = truck(15)
DAF = truck(18)
MAN.move()
DAF.move()

vaz = car(200)
lada = car(170)
vaz.move()
lada.move()