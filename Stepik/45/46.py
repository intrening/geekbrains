def inp():
    n = int(input())
    for _ in range(n):
        tn.append(input().lower())
    q = int(input())
    for _ in range(q):
        tq.append(input().lower())

tn, tq = [], []
n,q = 0,0
dic={}

#def opfi():
with open('/Users/nick/Documents/GitHub/geekbrains/Stepik/45/data.txt','r') as f:
    n = int(f.readline())
    for _ in range(n):
        tn.append(f.readline())
    q = int(f.readline())
    for _ in range(q):
        tq.append(f.readline())




    
for i in range(n): 
    s = tn[i].split()
    name = s[0]
    pars = [] if len(s)<=2 else s[2:]
    dic[name] = {'parents':pars,'childs':{name}}

def via_parents (name,child):
    for i in dic[name]['parents']:
        if dic.get(i):
            dic[i]['childs'].update([child])
        else:
            dic[i] = {'parents':[],'childs':{child}}
        via_parents (i,child)

for key,Value in dic.copy().items():
    via_parents (key,key)

childs = set()
printed = []
for i in range(q):
    s=tq[i].strip()
    if s in childs:
        if s not in printed:
            print (s)
            printed.append(s)
    else:
        if dic.get(s):
            childs.update (list(dic[s]['childs']))
            childs.update([s])
        
        
    