# Имеется список с произвольными данными. Необходимо преобразовать его в множество.
# Если какие-то элементы нельзя хешировать, то пропускаем их.  Результаты выведите на экран.

def list_to_set(list_in):
    _set = set()
    for i in list_in:
        try:
            _set.add(i)
        except Exception:
            pass
    return _set

result = list_to_set([1, [2], 46, 46, {1}, {2: 1}, (1, 2), 'qwerty', 3.45])  # for example
print(result)
