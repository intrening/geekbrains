with open('/Users/nick/Documents/GitHub/geekbrains/Stepik/data.txt', 'r', encoding='utf-8') as inf:
    text = inf.readlines()
text.reverse()
print (''.join(text))