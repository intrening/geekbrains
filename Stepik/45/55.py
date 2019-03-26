#s = 'MCMLXXXIV'
s = input()
s += ' '
n = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,' ':0}
sum = 0
for i in range(len(s)-2,-1,-1):
    if n[s[i]]<n[s[i+1]]:
        sum -= n[s[i]]
    else:
        sum += n[s[i]]
print (sum)