# 4) С клавиатуры в одной строке вводится произвольное количество вещественных чисел.
# Запишите их в файл, расположив каждое число на отдельной строке.


# a = [float(x) for x in input().split()]
#a = float(input('Введите произвольное количество вещественных чисел: '))
#with open('float.txt', 'w', encoding='utf-8') as f:
#    for i in a.split():
#        f.write(i)

a = (x for x in input('Введите произвольное количество вещественных чисел: ').split())
with open('float.txt', 'w', encoding='utf-8') as f:
    for i in a:
        f.write(i + '\n')

