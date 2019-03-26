import requests
import json

client_id = '69571ad97d2501ba1034'
client_secret = '5000138e774b2f03ffdf2f19d97cfc65'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]


s = """54521f9d7261691cea0f0300
537def3c139b21353f0006a6
4ff369de1083d40001002e2d
4df3ce2bd85a53000100243b
511294005c85615a61000082
4e96f7a9be2b4e0001003049
53208af2b202a3a1f900003c
554a78d87261692b00710400
50208d56f9f2e70002001409
53e126267261692d6bf50100
56d6f872139b2166eb000ade
4f20563c17014f0001000399
4f5f64c13b555230ac000004
55956e8d72616970d400002b
52cf3382275b2451fb00039e
"""

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
data = []
for i in s.split():
    i.strip()
    # инициируем запрос с заголовком
    r = requests.get("https://api.artsy.net/api/artists/"+i, headers=headers)

    # разбираем ответ сервера
    j = json.loads(r.text)
    data.append ([j['birthday'],j['sortable_name']])

data.sort()
for i in data:
    print (i[1])