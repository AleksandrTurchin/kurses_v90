str = input('Введите строку: ')

# use https://pythonru.com/osnovy/stroki-python  # Срезы-строк
task1_1 = str[2]
print(f'Третий символ: {task1_1}')  # output the third character

task1_2 = str[-2]
print(f'Предпоследний символ: {task1_2}')  # output the second to last character

task1_3 = str[:5]
print(f'Первые пять символов строки: {task1_3}')  # output the first five characters

task1_4 = str[:-2]
print(f'Строка, кроме последних двух символов: {task1_4}')  # output string except for the last two characters

task1_5 = str[::2]
print(f'Все символы с четными индексами: {task1_5}')  # output even characters

task1_6 = str[1::2]
print(f'Все символы с нечетными индексами: {task1_6}')  # output odd characters

task1_7 = str[::-1]
print(f'Все символы в обратном порядке: {task1_7}')  # output the characters in reverse order

task1_8 = str[::-2]
print(f'Все символы через один в обратном порядке: {task1_8}')  # output the characters in reverse order starting from the last through one

task1_9 = len(str)
print(f'Длина строки: {task1_9}')  # output the length of the string
