s = input()
x,y = map(int,s.split('/'))
l = []

def ost (x,y):
    l.append(x//y)
    return y, x%y
while y !=0:
    x,y = ost (x,y)

for i in l:
    print (i, sep = ' ')