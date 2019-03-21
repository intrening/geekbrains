# put your python code here

def upd_list(j):
    res = set(j)
    if j in dic.keys():
        for i in dic[j]:
            res.update (upd_list (i))
    return res


dic={}
#n=int(input())
n = 4
t = """A
B : A
C : A
D : B C""".split("\n")
for i in range(n): 
    #s = input().split()
    s = t[i].split()
    if len(s) <= 2:
        dic[s[0]]=set()
    else:
        if not s[0] in dic:
            dic[s[0]]=set()
        for j in s[2:]:
            dic[s[0]].update (j)

for i in dic.keys():
    upd = set()
    for j in dic[i]:
        upd.update(upd_list(j))
    dic[i].update(upd)

#q=int(input())
q = 4 
t = """A B
B D
C D
D A""".split("\n")
for i in range(q):
    #s=input().split()
    s=t[i].split()
    if len (s) > 1 and (s[0] in dic[s[1]] or s[0] == s[1]):
        print ('Yes')
    else:
        print ('No')