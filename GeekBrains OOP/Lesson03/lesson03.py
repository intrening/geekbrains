import os
# хороший кроссплатформенный метод указания пути:
path = os.path.realpath()
f = open(path, 'r', encoding='UTF-8')
# Считываем всю информацию из файла в виде списка строк
print(f.readlines())
f.close()