from player import Player
from hamsters import Hamster
import random


class Game:
    n = 10
    m = 10
    map = ("*"*m+"\n")*n
    hamsters_count = 4
    ways = ["a","s","d","w"]

    gameon = True
    def __init__(self):
        self.player = Player()
        self.hamsters =[]
        i = 0 
        while i < self.hamsters_count:
            h = Hamster (i, self.m,self.n)
            if self.get_humster_on_pos (h.pos) == "*":
                self.hamsters.append(h)
                i += 1
            

    def add_point (self, pos, name, s):
        li = s.split('\n')
        row = li[pos[1]]
        row = row[:pos[0]]+name+row[pos[0]+1:]
        li[pos[1]] = row
        return '\n'.join(li)


    def render_map (self):
        s = self.map
        for i in self.hamsters:
            if i.health > 0:
                s = self.add_point (i.pos, str(i.id), s)
        s = self.add_point (self.player.pos, "x", s)
        print(s)
    
    directions = {"w":"s","a":"d","d":"a","s":"w"}
    def on_move (self,dest):
        ham = self.get_humster_on_pos(self.player.pos)
        if not ham in ["*","\n"]:
            self.player.was_hit(self.hamsters[ham].health)
            killed = self.hamsters[ham].on_shot()
            print ("Players health: ", self.player.health)
            
            if self.player.health <= 0:
                self.gameon = False
                print ("GAME OVER")
                return False
            if not killed:
                print (str(ham) + " wasn't killed")
                self.move_player(self.player, self.directions[dest])
            else:
                print (str(ham) + " was killed")
                self.hamsters_count -= 1

            

    def get_humster_on_pos (self, coords):
        for i in self.hamsters:
            if i.pos == coords and i.health > 0:
                return i.id
        return ("*")


    def move_player (self, obj, dest):
        if dest == "s":
            if obj.pos[1] == len(self.map.split('\n')) - 2:
                return False
            obj.pos[1] += 1
        if dest == "w":
            if obj.pos[1] == 0:
                return False
            obj.pos[1] -= 1
        if dest == "a":
            if obj.pos[0] ==0:
                return False
            obj.pos[0] -= 1
        if dest == "d":
            if obj.pos[0] == len(self.map.split('\n')[0]) - 1:
                return False
            obj.pos[0] += 1

    def start(self):
        self.render_map()
        while self.gameon:
            if self.hamsters_count == 0:
                print ("YOU ARE CHAMPION!")
                break
            command = input ("Insert command:")
            if command in self.ways:
                self.move_player(self.player,command)
                self.on_move(command)
            if command == "e":
                self.player.wait()
            for i in self.hamsters:
                self.move_player(i,random.choice(self.ways))
            self.render_map()


game = Game()
game.start()