import requests
import re

#a = input()
a = 'https://ob1.ru'
a = "http://pastebin.com/raw/hfMThaGb"

text = requests.get(a).text
pattern = re.compile(r'<a.*?href=[\"\']\b.*?([\w\.\_\-]*\.\w+).*[\"\']')
res = list(set(pattern.findall(text)))
res.sort()
for i in res:
    print (i)
