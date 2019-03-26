class ExtendedStack(list):
    def sum(self):
        # операция сложения
        self.append(self.pop()+self.pop())

    def sub(self):
        # операция вычитания
        self.append(self.pop() - self.pop())
    
    def mul(self):
        # операция умножения
        self.append(self.pop()*self.pop())

    def div(self):
        # операция целочисленного деления
        self.append(self.pop()//self.pop())

import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list,Loggable):
    def append(self,obj):
        super().append(obj)
        self.log(obj)

l = LoggableList()
l.append(2)