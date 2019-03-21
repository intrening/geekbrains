import random
def supersort(item):
    if item%2 == 0:
        return item
    else:
        return -item
a = [
    [1,2,0],
    [3,5,201],
    [8,6,100]
]
for row,line in enumerate(a):
    print (line)
print()
c = []
b = sorted(a, key=lambda x: -x[0])
for row,line in enumerate(a):
    c += line

print (c)
c.sort(key=supersort)
print (c)
