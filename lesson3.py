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
    return int(x*a[1] + a[0]*y), int(y*a[1])

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

s = input ()
s = s.split(' ')
i,a = 0,[]
a.append([1,0])
for n in s:
    if is_number(n):
        a[i][0] *= int(n)
        a[i][1] = 1
    elif n == '-':
        i += 1
        a.append([-1,0])
    elif n == '+':
        i += 1
        a.append([1,0])
    else:
        x,y = map(int, n.split('/'))
        if a[i][1] == 0:
            a[i][0] = x*a[i][0]
            a[i][1] = y
            
        else:
            if a[i][0] > 0:
                a[i][0] = a[i][0]*y + x
            else:
                a[i][0] = a[i][0]*y - x
            a[i][1] = y

x,y = 0,1
for i in a:
    x,y = sumA(x,y,i)

i = 1
p = []
while i < abs(x) and i < abs(y):
    p.append(i)
    for j in p:
        if i%j == 0:
            i += 1
    if x%i == 0 and y%i == 0:
        x = int(x/i)
        y = int(y/i)

s = ""
if x == 0:
    s = '0'

if abs(x)//y != 0:
    if x < 0:
        s = str(x//y+1) + ' '
    else:
        s = str(x//y) + ' '

if abs(x)%y > 0:
    if x<0:
        s += '-{}/{}'.format(abs(x)%y,abs(y))
    else:
        s += '{}/{}'.format(abs(x)%y,abs(y))
    
print(s)


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

d = {}
with open ('data/workers','r',encoding='utf-8') as inf:
    inf.readline()
    for s in inf:
        s = s.split()
        d[s[0] + ' ' + s[1]] = s[2],s[4]

with open ('data/hours_of','r',encoding='utf-8') as inf:
    inf.readline()
    for s in inf:
        s = s.split()
        salary = float(d[s[0] + ' ' + s[1]][0])
        norm = float(d[s[0] + ' ' + s[1]][1])
        works = float(s[2])
        for_hour = salary/norm
        if works > norm:
            result = salary + (works-norm)*2*for_hour
        elif works < norm:
            result = salary - (norm-works)*for_hour
        else:
            result = salary
        print (s[0] + ' ' + s[1], round(result,2))


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

d = {a: [] for a in list (map(chr, range(ord('А'), ord('Я')+1)))}
with open ('data/fruits', 'r', encoding='utf-8') as inf:
    for n in inf:
        s = n.strip()
        if s != '':
            d[s[0]].append(s)

for key in d.keys():
    if len (d[key]) >0:
        s = 'data/fruits_' + key
        with open (s, 'w', encoding='utf-8') as inf:
            for i in d[key]:
                inf.write(i + '\n')