#Волосянков Николай

#EASY
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import sys

def new_dir(dir):
    try:
        os.mkdir (dir)
    except FileExistsError:
        print (dir + " уже существует!")

def del_dir(dir):
    try:
        os.rmdir (dir)
    except FileNotFoundError:
        print (dir + " не существует!")
    except OSError:
        print (dir + " не пустая папка, удаление невозможно")

for i in range(1,10):
    new_dir("dir_" + str(i))

for i in range(1,10):
    del_dir ("dir_" + str(i))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def show_dir():
    for i in os.listdir(os.path.curdir):
        if os.path.isdir(i):
            print (i)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
print ()
with open (sys.argv[0],"r") as inf:
    f = inf.read()
with open (sys.argv[0] + "_copy","w") as inf:
    inf.write(f)
