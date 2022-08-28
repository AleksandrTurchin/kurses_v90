# Написать функцию-декоратор, которая вычисляет время выполнения декорируемой функции,
# а также выводит на экран имя функции и ее параметры.

from inspect import signature
# import inspect

"""import time
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))"""   # https://askdev.ru/q/kak-poluchit-vremya-vypolneniya-programmy-python-1330/

from datetime import datetime
def decorating_func(own_func):
    def wrapper(*args, **kwargs):
        time_now = datetime.now()
        result = own_func(*args, **kwargs)
        print(f'Время выполнения декорируемой функции: {datetime.now() - time_now}')
        print(f'Имя функции: {own_func.__name__}')                                      # __name__ or __qualname__
        print(f'Параметры функции: {signature(own_func)}')                              #https://docs.python.org/3/library/inspect.html#introspecting-callables-with-the-signature-object
        return result
    return wrapper


@decorating_func
def sum_range(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end + 1))


print(sum_range(1, 10009000))

