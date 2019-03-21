s = input()
a = input()
b = input()

for i in range(0,1001):
    s0 = s
    s = s.replace(a,b)
    if s0 == s and not a in s:
        break

if i == 1000:
    print ('Impossible')
else:
    print (i)
