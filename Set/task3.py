# Предоставлен список натуральных чисел.
# Требуется сформировать из них множество.
# Если какое-либо число повторяется, то преобразовать его в строку по образцу:
# например, если число 4 повторяется 3 раза,
# то в множестве будет следующая запись:
# само число 4, строка «44» (второе повторение, т.е. число дублируется в строке),
# строка «444» (третье повторение, т.е. строка множится на 3).
# Результаты выведите на экран.

list_in = [1, 2, 3, 4, 4, 5, 6, 4, 7]
i = 0
while i < len(list_in):
    x = list_in.count(list_in[i])
    if x > 1:
        list_in[i] = str(list_in[i]) * x
    i += 1
print(set(list_in))
