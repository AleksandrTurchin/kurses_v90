# Дан список. Необходимо удалить пустые строки из списка. Результаты вывести на экран.
_list = [1, 2, 3, '', 5]
print([i for i in filter(None, _list)])


# Дан список чисел. Превратите его в список квадратов этих чисел. Результаты вывести на экран.
_list = [1, 2, 3, 4, 5]
print([i ** 2 for i in _list])


# Дан список чисел, необходимо удалить все вхождения числа 20 из него. Результаты вывести на экран.
_list = [1, 2, 3, 20, 4, 5, 20, 6]
print([i for i in _list if i != 20])


# Дан список. Необходимо вывести список в обратном порядке.
_list = [1, 2, 3, 4, 5]
_list.reverse()
print(_list)


# Дан список. Необходимо поменять местами самый большой и самый маленький элементы списка. Результаты вывести на экран.
_list = [1,2,33,4,5]
max_element = max(_list)
min_element = min(_list)
index_max_element = _list.index(max_element)
index_min_element = _list.index(min_element)
_list[index_max_element], _list[index_min_element] = _list[index_min_element], _list[index_max_element]
print(_list)

print()
# Дан список. Необходимо определить, есть ли в списке повторяющиеся элементы, если да, то вывести на экран это значение.
_list = [1, 2, 3, 4, 4, 5]
for i in _list:  # ???????????????????????
    if _list.count(i) == 1:
        break
print(i)
# print([i for i in _list if _list.count(i) >= 1]) - ?????????????????????????????


#  Дан список. Необходимо найти сумму и произведение элементов списка. Результаты вывести на экран.
_list = [1, 2, 3, 4, 5]
print(sum(_list))
x = 1
for i in _list:
    x *= i
print(x)

