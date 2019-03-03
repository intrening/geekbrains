# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def sumA(x,y,a):
    return int(x*a[1] + a[0]*y), int (y*a[1])

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

#input (s)
s = "0"
s = s.split(' ')
i,a = 0, []
a.append([1,0])
for n in s:
    if is_number(n):
        a[i][0] *= int(n)
        a[i][1] = 1
    elif n == '-':
        i+=1
        a.append([-1,0])
    elif n == '+':
        i+=1
        a.append([1,0])
    else:
        x,y = map (int, n.split('/'))
        if a[i][1] == 0:
            a[i][0] = x*a[i][0]
            a[i][1] = y
            
        else:
            if a[i][0] >0:
                a[i][0] =a[i][0]*y + x
            else:
                a[i][0] =a[i][0]*y - x
            a[i][1] = y

x,y = 0,1
for i in a:
    x, y = sumA(x,y,i)

i = 1
p = []
while i < abs(x) and i < abs(y):
    p.append(i)
    for j in p:
        if i%j == 0:
            i+=1
    if x%i == 0 and y%i == 0:
        x = int(x/i)
        y = int(y/i)


s = "0"

if abs(x)//y != 0:
    if x<0:
        s = str(x//y+1) +' '
    else:
        s = str(x//y) + ' '

if abs(x)%y:
    if x<0:
        s += '-{}/{}'.format(abs(x)%y,abs(y))
    else:
        s += '{}/{}'.format(abs(x)%y,abs(y))
    
#print (s)



# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

with open ('/Users/nick/Documents/GitHub/geekbrains/data/workers','r',encoding='utf-8') as inf:
    for s in inf:
        print (s.split())