#моя домашка
import re

#1. Получите текст из файла.
with open ('/Users/nick/Documents/GitHub/worklog/GeekBrains OOP/Lesson01/data.txt') as inf:
    text = inf.read()


#2. Разбейте текст на предложения.
pattern = r"\.\s|\?\s|\!\s"
text2 = re.sub(pattern,'/n',text)


#3. Найдите самую используемую форму слова, состоящую из 4 букв и более, на русском языке.
pattern = r"[А-я]{4,}"
words = re.findall(pattern,text)

d={}
max_count=0
max_word=''

for word in words:
    word=word.lower()
    for i in range(0,len(word)-4):
        for n in range(4,len(word)-4):
            st=word[i:i+n]
            if st not in d:
                d[st]=1
            else:
                d[st]+=1
            if max_count<d[st]:
                max_count=d[st]
                max_word=st
#max_word - максимальная форма слова


#4. Отберите все ссылки.
pattern_links=re.compile(r"http[s]?:\/\/[\w\.\/\?\=\&]+[^\s\.\?\!]|www.[\w\.\/\?\=\&]+[^\s\.\?\!]|[\w]+\.[\w\.\/\?\=\&]+[^\s\.\?\!]")
text4 = pattern_links.findall(text)


#5. Ссылки на страницы какого домена встречаются чаще всего?
pattern = r"(\w+\.\w+)[\/\s\?]"
text5=re.findall(pattern,text)

from collections import Counter
dic=Counter(text5)

max_domain = ''
max_count = 0
for i in dic:
    if dic[i] > max_count:
        max_domain = i
        max_count = dic[i]
#max_domain - домен, ссылки на который встречаются чаще всего


#6. Замените все ссылки на текст «Ссылка отобразится после регистрации».
text6=pattern_links.sub('«Ссылка отобразится после регистрации»',text)



#Правильное выполнение
import re

#1. Получите текст из файла.
with open ('/Users/nick/Documents/GitHub/worklog/GeekBrains OOP/Lesson01/data.txt') as inf:
    text = inf.read()


#2. Разбейте текст на предложения.
pattern = r"[\.\?!]\s+"
text2 = re.split(pattern,text)


#3. Найдите самую используемую форму слова, состоящую из 4 букв и более, на русском языке.
pattern = r"[А-я]{4,}"
words = re.findall(pattern,text)


d={}
max_count=0
max_word=''

for word in words:
    word=word.lower()
    for i in range(0,len(word)-4):
        for n in range(4,len(word)-4):
            st=word[i:i+n]
            if st not in d:
                d[st]=1
            else:
                d[st]+=1
            if max_count<d[st]:
                max_count=d[st]
                max_word=st
#max_word - максимальная форма слова


#4. Отберите все ссылки.
pattern_links=re.compile(r"http[s]?:\/\/[\w\.\/\?\=\&]+[^\s\.\?\!]|www.[\w\.\/\?\=\&]+[^\s\.\?\!]|[\w]+\.[\w\.\/\?\=\&]+[^\s\.\?\!]")
text4 = pattern_links.findall(text)


#5. Ссылки на страницы какого домена встречаются чаще всего?
pattern = r"(\w+\.\w+)[\/\s\?]"
text5=re.findall(pattern,text)

from collections import Counter
dic=Counter(text5)

max_domain = ''
max_count = 0
for i in dic:
    if dic[i] > max_count:
        max_domain = i
        max_count = dic[i]
#max_domain - домен, ссылки на который встречаются чаще всего


#6. Замените все ссылки на текст «Ссылка отобразится после регистрации».
text6=pattern_links.sub('«Ссылка отобразится после регистрации»',text)