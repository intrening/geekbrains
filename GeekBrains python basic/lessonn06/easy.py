#Волосянков

# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)
 
# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car ():
    def __init__(self, name=''):
        self.speed = 0
        self.color = 'black'
        self.name = name
        self.is_police = False
        pass
    def go(self):
        pass
    def stop (self):
        pass
    def turn (self, direction):
        pass

class TownCar (Car):
    pass

class SportCar(Car):
    pass

class WorkCar(Car):
    pass

class PoliceCar(Car):
    def __init__(self, name=''):
        super().__init__(name)
        self.is_police = True

a = PoliceCar('Mycar')
a.speed = 333