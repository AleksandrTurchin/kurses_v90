# Имеется список с произвольными данными. Необходимо преобразовать его в множество.
# Если какие-то элементы нельзя хешировать, то пропускаем их.  Результаты выведите на экран.

def list_to_set(list_in):
    _set = set()            # создаем переменную множества, куда будем добавлять данные из списка list_in
    for i in list_in:
        try:                # с помощью set.add(item) добавляем данные из списка list_in, а try-except отлавливаем TypeError
            _set.add(i)
        except TypeError:
            pass
    return _set

result = list_to_set([1, [2], 46, 46, {1}, {2: 1}, (1, 2), 'qwerty', 3.45])  # for example
print(result)
# {1, 3.45, (1, 2), 'qwerty', 46}