# 1) Напишите программу, которая принимает поисковый запрос и выводит названия текстовых файлов,
# содержащих искомую подстроку. Все файлы располагаются в заданной директории.
import os
folder = 'C:\\Users\\37529\\PycharmProjects\\exercises_28.07.2022'  # директория с файлами
answer = set()                                                                   # если подстрока может встречаться в одном и том же файле несколько раз используем set
search = input('Input the search string:')                                       # для примера: dict
for filename in os.listdir(folder):                                              # итерируемся по списку (получили с помощью os.listdir) c именами файлов в заданной директории (file.txt, text.txt, text.txt)
    filepath = os.path.join(folder, filename)                                    # для каждого файла получили путь для метода open()
    with open(filepath, 'r', encoding='utf-8') as f:                             # открываем каждый файл для чтения
        for line in f:                                                           # итерируемся по строкам каждого файла
            if search in line:                                                   # ищем искомую подстроку в каждой строке каждого файла
                answer.add(filename)                                             # добавляем имена файлов, содержащих искомую строку, в множество set
for i in answer:                                                                 # итерируемся по множеству set, чтобы вывести названия текстовых файлов, содержащих искомую подстроку
    print(i)

