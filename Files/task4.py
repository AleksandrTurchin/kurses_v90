# 4) С клавиатуры в одной строке вводится произвольное количество вещественных чисел.
# Запишите их в файл, расположив каждое число на отдельной строке.

float_numbers = input('Input the search string:').split()

# float_numbers = ('1 2 3 4 5 6 7 8 8 8888').split()  # for example

with open('float.txt', 'w', encoding='utf-8') as f:
    for i in float_numbers:
        f.write(i + '\n')
