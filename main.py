import os
import shutil
from pathlib import Path

# change working directory
os.chdir("/Users/kirillanpilov/PycharmProjects/file_manager")
menu = '''
1. Создание папки (с указанием имени);
2. Удаление папки по имени;
3. Перемещение между папками (в пределах рабочей папки) - заход в папку по имени, выход на уровень вверх;
4. Создание пустых файлов с указанием имени;
5. Запись текста в файл;
6. Просмотр содержимого текстового файла;
7. Удаление файлов по имени;
8. Копирование файлов из одной папки в другую;
9. Перемещение файлов;
10. Переименование файлов.
11. Выход из программы
'''

while True:
    print("Вы находитесь в директории", os.getcwd())
    print("Текущие файлы", os.listdir())
    print(menu)
    choice = int(input("Выбирите пункт в меню: "))
    if choice == 1:
        os.mkdir(input("Введите имя папки: "))
    if choice == 2:
        os.rmdir(input("Введите имя папки: "))
    if choice == 3:
        os.chdir(input("Ввыдите имя папки в которую хотите перейти"))

    if choice == 4:
        file_name = input("Введите название файла: ")
        file = open(file_name, 'w')

    if choice == 5:
        file_name = input("Введите название файла: ")
        with open(file_name, "w") as file:
            print("Вводите текст в файл")
            text = input()
            file.write(text)

    if choice == 6:
        file_name = input("Введите название файла: ")
        with open(file_name, 'r') as file:
            lines = file.readlines()
            print("В файле ", file_name)
            for i in lines:
                print(i)

    if choice == 7:
        file_name = input("Введите название файла: ")
        os.remove(file_name)

    if choice == 8:
        file_name = input("Введите название файла, который хотите скопировать: ")
        dict_name = input("В какую папку хоитите скопировать: ")
        shutil.copy(file_name,dict_name)

    if choice == 9:
        pass

    if choice == 10:
        file_name = input("Введите название файла, который хотите переименовать: ")
        new_file_name = input("Введите новое название файла: ")
        os.rename()
    if choice == 11:
        break


