#Получить количество учеников с сайта geekbrains.ru:
#используя регулярные выражения,
#используя библиотеку BeautifulSoup.

import re as re
from bs4 import BeautifulSoup as BS
import requests
req = requests.get('https://geekbrains.ru')
text = req.text

# поиск количества с помощью re
pattern = r'<span class=\"total-users\">Нас уже (.+) человек<\/span>'

n=re.findall(pattern,text)
print ('Количество учеников: ' + n[0])

# поиск количества с помощью bs4

s = BS (text,"html.parser")
n = s.findAll(attrs={"class":"total-users"})[0].text
n = ''.join (re.findall(r'\d',n))
print ('Количество учеников: ' + n)


