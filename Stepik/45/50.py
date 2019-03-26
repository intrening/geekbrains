import requests
import json
import sys

s = """928
954
930
962
932
900
999
940
910
943
976
977
918
950
922""".split()

for n in s:
    n = n.strip()
    if not n:
        continue
    r = requests.get("http://numbersapi.com/"+n+"/math?json=true")
    j = json.loads(r.text)
    if not j['found']:
        print ('Boring')
    else:
        print('Interesting')

