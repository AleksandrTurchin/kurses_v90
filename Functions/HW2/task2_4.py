# Имеется список с произвольными данными. Необходимо преобразовать его в множество.
# Если какие-то элементы нельзя хешировать, то пропускаем их.
# Результаты выведите на экран. Использовать lambda-функции.

from collections.abc import Hashable                            # https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable

def list_to_set(_list):
    _set = filter(lambda x: isinstance(x, Hashable), _tuple)    # https://docs.python.org/3/library/functions.html#isinstance
                                                                # https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-isinstance/
    return set(_set)

# Тесты
_tuple = (1, [2])
print(list_to_set(_tuple))
