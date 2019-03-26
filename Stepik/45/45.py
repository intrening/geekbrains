dic={}
#n=int(input())
n = 2
t = """A : C B
B : D E""".split("\n")
for i in range(n): 
    #s = input().split()
    s = t[i].split()
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

#q=int(input())
q = 1 
t = """E A """.split("\n")
for i in range(q):
    #s=input().split()
    s=t[i].split()
    if len (s) > 1 and dic.get(s[0]) and s[1] in dic[s[0]]['childs']:
        print ('Yes')
    else:
        print ('No')

