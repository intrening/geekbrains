import json

def via_parents (name,child):
    for i in dic[name]['parents']:
        dic[i]['childs'].update([child])
        via_parents (i,child)

#j = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "D", "parents": ["C"]}]'
#j = '[{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, {"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]'
j = input()
data = json.loads(j)
dic = {}
for i in data:
    dic[i['name']] = {'childs':{i['name']},'parents':i['parents']}

for key,Value in dic.items():
    via_parents (key,key)

res = []
for key,Value in dic.items():
    res.append([key,len (Value['childs'])])

res.sort()
for i in res:
    print (i[0],':',i[1])
    
