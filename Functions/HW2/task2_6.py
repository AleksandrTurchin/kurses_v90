# Напишите генератор custom_range(start, end, step),
# который генерирует все целые числа от значения «start» до величины «end» включительно с шагом «step».
# Если пользователь задаст первое число большее чем второе, просто поменяйте их местами. «step» по умолчанию равен = 0.
# Также не допускать ввод дробных чисел.

def custom_range(start, end, step):
    if start > end:
        start, end = end, start

    yield from range(start, end + 1, step)

gen = custom_range(1, 10, 2)
for i in gen:
    print(i)

