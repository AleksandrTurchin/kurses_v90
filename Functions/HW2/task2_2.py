# Напишите функцию inspect_function(),
# которая в качестве аргумента принимает другую функцию (главное, не встроенную, built-in).
# В результате работы она выводит следующие данные: название анализируемой функции,
# наименование всех принимаемых ею параметров и их типы (позиционные, ключевые и т.п.).

import inspect
import math


def inspect_function(some_func):
    print(f'Анализируем функцию {some_func.__name__}')
    for param in inspect.signature(some_func).parameters.values():
        print(param.name, param.kind, sep=': ')

# Функция для анализа
def my_func(a, b, /, c, d, *args, e, f, **kwargs):
    pass

# Тесты
inspect_function(my_func)
print('-' * 25)
inspect_function(math.sqrt)
