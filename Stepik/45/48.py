import simplecrypt

with open("/Users/nick/Documents/GitHub/geekbrains/Stepik/45/encrypted.bin", "rb") as inp:
    encrypted = inp.read()

with open("/Users/nick/Documents/GitHub/geekbrains/Stepik/45/passwords.txt", "r") as f:
    pas = f.read().split('\n')

for i in pas:
    try:
        print (simplecrypt.decrypt(i,encrypted))
        print ('Подошел: ',i)
    except:
        print ('Не подходит: ',i)
