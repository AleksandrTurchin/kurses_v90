# Имеется список с произвольными данными. Необходимо преобразовать его в множество.
# Если какие-то элементы нельзя хешировать, то пропускаем их.  Результаты выведите на экран.

_list = [1, [2], 46, 46, {1}, {2: 1}, (1, 2), 'qwerty', 3.45]

# _set = {}
_set = set()
for i in _list:
    try:
        _set.add(i)
    except (AttributeError, TypeError):
        pass
print(_set)
