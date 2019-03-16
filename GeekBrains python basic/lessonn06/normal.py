# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person:
    def __init__(self, name='', health=100, damage = 50, armor = 1):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
    def beat(self, damage):
        self.health -= int(damage/self.armor)
    def getInfo (self):
        print ('Имя: ', self.name)
        print ('Здоровье: ', self.health)
        print ('Урон: ', self.damage)
        print ('Броня: ', self.armor)

class Player(Person):
    def attack(self, enemy):
        enemy.beat (self.damage)

class Enemy (Person):
    def attack(self, player):
        player.beat (self.damage)


p1 = Player(name = "Игрок", armor=2)
p2 = Enemy(name = "AI", damage=77)
while p1.health > 0 and p2.health >0:
    p1.attack(p2)
    if p2.health <=0:
        break
    p2.attack (p1)
print ('Победитель:')
if p1.health <0:
    p2.getInfo()
else:
    p1.getInfo()

