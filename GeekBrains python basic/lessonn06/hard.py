# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

class Fabric:
    def __init__(self):
        pass
    def make_game(self, name, color, typ=''):
        if typ == 'animal':
            return Animal(name, color, typ)
        elif typ == 'person':
            return Person(name, color, typ)
        else:
            return None

class Game:
    def __init__(self, name='',color='black',typ='animal'):
        self.name, self.color, self.type = name, color, typ
        self._bying()
        self._make()
        self._color()

    def _bying (self):
        print ('Закупаю сырье для ' + self.name)

    def _make (self):
        print ('Пошив для ' + self.name)
    def _color (self):
        print ('Покраска ' + self.name)

class Animal (Game):
    pass

class Person (Game):
    pass

f = Fabric()
new_game = f.make_game ('Игрушка №1', 'red','person')