s = input()
t = input()

i = 0
j = 0
while 0 <= i < len(s)-len(t)+1:
    i = s.find(t,i)
    if i == -1:
        break
    else:
        j += 1
        i += 1

print (j)