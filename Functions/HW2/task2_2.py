# Напишите функцию inspect_function(),
# которая в качестве аргумента принимает другую функцию (главное, не встроенную, built-in).
# В результате работы она выводит следующие данные: название анализируемой функции,
# наименование всех принимаемых ею параметров и их типы (позиционные, ключевые и т.п.).

from inspect import signature                                           # https://docs.python.org/3/library/inspect.html#introspecting-callables-with-the-signature-object
import math

def inspect_function(some_func):
    print(f'Анализируем функцию {some_func.__name__}')                  # __name__ or __qualname__
    for param in signature(some_func).parameters.values():
        print(param.name, param.kind, sep=': ')                         # https://www.geeksforgeeks.org/python-sep-parameter-print/

# Функция для анализа
def my_func(a, b, /, c, d, *args, e, f, **kwargs):
    pass

# Тесты
inspect_function(my_func)
print()
inspect_function(math.sqrt)
