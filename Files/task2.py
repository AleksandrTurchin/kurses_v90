# 2) Имеется файл file.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту:
# а) количество букв латинского алфавита;
# б) число слов;
# в) число строк.

words = 0                                                       # счетчик слов
letters_abc = 0                                                 # счетчик букв латинского алфавита
strings = 0                                                     # счетчик строк
with open('file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        strings += 1
        words += len(line.split())                              # .split() делит строку на подстроки (слова)
        letters_abc += len([i for i in line if i.isalpha()])    # генератор позволяет итерироваться по символам строки, а условие .isalpha() отсеивает все, кроме букв
    print(strings)
    print(words)
    print(letters_abc)
