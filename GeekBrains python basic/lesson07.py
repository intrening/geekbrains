#!/usr/bin/python3

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html
"""
import random

def random_list (num_list,k):
    s = set (num_list)
    res = []
    for _ in range(0,k):
        numb = random.choice(list(s))
        res.append(numb)
        s.remove(numb)
    return res


class NumberCard(list):

    def __init__ (self):
        self._generate_card()
        
    def _generate_card(self):
        nums = random_list (range(1,91),k=27)
        self.card = []
        for i in range(3):
            line = nums[i*9:(i+1)*9]
            line.sort()
            dels_nums = random_list (range(0,9),k=4)
            for j in dels_nums:
                line [j] = 0
            self.card += line + [-2]

    def print (self):
        br = "-"*26
        for i in self.card:
            if i == 0:
                print ('   ',end='')
            elif i == -1:
                print (' - ',end='')
            elif i == -2:
                print()
            elif len(str(i)) == 1:
                print (' ', i,' ',sep='',end='')
            else:
                print(i,' ',sep='',end='')
        print (br)

    def __contains__(self,value):
        if value in self.card:
            return True
        else:
            return False

    def delete (self,value):
        self.card[self.card.index(value)] = -1

    def __eq__ (self,value):
        return value == len(list(filter(lambda x:x>0,self.card)))

class Game():
    def __init__(self):
        self.restart()

    def restart(self):
        self.game_on = True
        self.no_winner = False
        self.series = random_list(range(1,91),90)
        self.player = NumberCard()
        self.ai = NumberCard()     
        print ("== Welcome to LOTO! ==")
        self.game_process()
    
    def print_lists(self):
        print ('------ Ваша карточка -----')
        self.player.print()
        print ('-- Карточка компьютера ---')
        self.ai.print()

    def game_process(self):
        for i in range(89,0,-1):
            b = self.series[i-1]
            print()
            print ('Новый бочонок: {} (осталось {})'.format(str(b),str(i)))
            self.print_lists()
            inp=""
            while inp not in ['n','N','y','Y']:
                inp = input ('Зачеркнуть цифру? (y/n) ')
            if b in self.player and inp in ['n','N']:
                self.game_on = False
                break
            if b not in self.player and inp in ['y','Y']:
                self.game_on = False
                break

            if b in self.player:
                self.player.delete(b)
            if b in self.ai:
                self.ai.delete(b)

            if self.player == 0 and self.ai == 0:
                self.no_winner = True
            if self.player == 0:
                break
            if self.ai == 0:
                self.game_on = False
                break
        if self.no_winner:
            print ("НИЧЬЯ!")
        else:
            if self.game_on:
                print ("YOUR ARE WINNER!")
            else:
                print ("GAME OVER")

        self.restart()

g = Game() 