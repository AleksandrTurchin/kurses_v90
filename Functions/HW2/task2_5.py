# Написать функцию-декоратор, которая вычисляет время выполнения декорируемой функции,
# а также выводит на экран имя функции и ее параметры.

import inspect
from datetime import datetime


def decorating_func(own_func):
    def wrapper(*args, **kwargs):
        time_now = datetime.now()
        result = own_func(*args, **kwargs)
        print(f'Время выполнения декорируемой функции: {datetime.now() - time_now}')
        print(f'Имя функции: {own_func.__qualname__}')
        print(f'Параметры функции: {inspect.signature(own_func)}')
        return result
    return wrapper


@decorating_func
def sum_range(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end + 1))


print(sum_range(1, 1000900))

