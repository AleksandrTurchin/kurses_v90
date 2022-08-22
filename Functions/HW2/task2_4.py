# Имеется список с произвольными данными. Необходимо преобразовать его в множество.
# Если какие-то элементы нельзя хешировать, то пропускаем их.
# Результаты выведите на экран. Использовать lambda-функции.

from collections.abc import Hashable

def list_to_set(_list):
    _set = filter(lambda x: isinstance(x, Hashable), _tuple)
    return set(_set)

# Тесты
_tuple = (1, [2])
print(list_to_set(_tuple))
