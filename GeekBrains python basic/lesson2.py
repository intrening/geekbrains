# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x - 11111140.2121'
x = 2.5
# вычислите и выведите y
eq = equation.split(' ')
k = float(eq[2][:-1])
b = float(eq[4])
if eq[3] == '-':
    b = -b
y = k*x + b
print (y)


# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
#date = '01.11.1985'
# Примеры некорректных дат
#date = '01.22.1001'
#date = '1.12.1001'

date = '-2.10.3001'

max_days=(31,28,31,30,31,30,31,31,30,31,30,31)
date=date.split('.')
err=0

try:
    month=int(date[1])
    if not (month >= 1 and month <= 12) or (len(date[1]) != 2):
        err=1
except:
    err=1

try:
    day=int(date[0])
    if not (day >= 1 and day <= max_days[month]) or (len(date[0]) != 2):
        err=1
except:
    err=1

try:
    year=int(date[2])
    if not (year >= 1 and year <= 9999) or (len(date[2]) != 4):
        err=1
except:
    err=1

if err:
    print ('Дата некорректна')
else:
    print ('Дата корректна')


# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

n = 2

x,y,stage = 0,0,0
while x < n:
    stage+=1
    x +=stage*stage
    y +=stage

y = y - (x-n)//stage
x = n%stage+1
print (y,x)
print ()