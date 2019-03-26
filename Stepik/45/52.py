import re
a = input()
b = input()
l = []
for i in range(len(a)-len(b)+1):
    if a[i:].startswith(b):
        l.append(i)
if l:
    for i in l:
        print (i, end=' ')
else:
    print(-1)

print()