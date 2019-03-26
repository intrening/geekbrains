import re
def inp():
    global s
    try:
        while True:
            inp = input()
            s.append(inp)
    except:
        None

def op_file():
    global s   
    with open('/Users/nick/Documents/GitHub/geekbrains/Stepik/45/data.txt','r') as f:
        for i in f.readlines():
            s.append(i.strip())


s = []
inp()

for i in s:
    if not i.isdigit():
        continue
    pattern = re.compile(r'([0,1][0,1]?)')
    p = pattern.findall(i)
    if p != []:
        even = sum (int(j[0]) for j in p)
        noteven = sum (int(j[1]) for j in p if len(j)>1)
        if (even - noteven)%3 ==0:
            print (i) 
    