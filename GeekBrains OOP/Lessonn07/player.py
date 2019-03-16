import random

class Player:
    health = 10
    max_health = 10
    defaul_damage = 10
    pos =[0,0]
    
    def was_hit(self,h):
        self.health -= random.choice(range(h+1))
    
    def wait (self):
        if self.health < self.max_health:
            self.health += 1
            print ("Players health: ", self.health)