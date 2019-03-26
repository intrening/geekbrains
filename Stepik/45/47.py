class multifilter:
    def judge_half(self,pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        res = True if pos >= neg else False
        return res


    def judge_any(self,pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        res = True if pos >= 1 else False
        return res


    def judge_all(self,pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        res = True if neg ==0 else False
        return res

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        for i in self.iterable:
            res,pos,neg = [],0,0
            for j in self.funcs:
                res.append(j(i))
            pos = sum(1 for k in res if k)
            neg = sum(1 for k in res if not k)
            if self.judge(self,pos,neg):
                yield i
            
def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)] # [0, 1, 2, ... , 30]
#print(list(multifilter(a, mul2,judge=multifilter.judge_all)))

#print(list(multifilter(a, mul2, mul3, mul5))) 
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

#print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half))) 
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

#print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all))) 
# [0, 30]


import itertools
import math
def primes():
    a = 1
    while True:  # просто пример
        a += 1
        if (math.factorial(a-1)+1)%a == 0:
            yield a

print(list(itertools.takewhile(lambda x : x <= 10, primes())))
