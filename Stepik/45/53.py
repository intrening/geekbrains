li = [chr(i) for i in range(128512, 128592)]
a = ''.join(li)
#n = int(input())
#s = input().strip()
s = '😀🙏😇'
n = 1

n = n%len(a)
s2 = ''
for i in s:
    pos = a.find(i) + n
    if pos >= len(a)-1:
        pos -= len(a)-1
    if pos <0:
        pos += len(a)
    s2 += a[pos]
print ('Result: "', s2, '"',sep='')
    