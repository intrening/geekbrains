from random import randint
class Hamster:
    pos = [0,0]
    health = 1

    def __init__(self, id, map_width, map_height):
        self.health = 2
        self.pos = [randint(0,map_width-1),randint(0,map_height-1)]
        self.id = id

    def on_shot (self):
        self.health -=1
        return self.health <= 0
             

