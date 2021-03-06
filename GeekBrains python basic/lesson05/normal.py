#NORMAL
# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import easy
import os

def goto_dir():
    dir = input('Введите директорию: ')
    try:
        os.chdir(dir)
    except FileNotFoundError:
        print ("Директория не существует!")

def menu():
    do = {"1": goto_dir,
          "2": easy.show_dir,
          "3": easy.del_dir,
          "4": easy.new_dir
          }
    while True:
        print ('Текущая директория:')
        print (os.getcwd())
        print ('***************************\n'
            'Выберите действие:\n'
            '1. Перейти в папку\n'
            '2. Просмотреть содержимое текущей папки\n'
            '3. Удалить папку\n'
            '4. Создать папку\n'
            '5. Выход\n'
            '***************************')
        select =  input("Ваш выбор:")
        if select in ['1','2']:
            do[select]()
        elif select == '3':
            do[select](input("Введите название папки для удаления:"))
        elif select == '4':
            do[select](input("Введите название папки:"))                
        elif select == '5':
            break
        else:
            print ('Неизвестная команда')
menu()