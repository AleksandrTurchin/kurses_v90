# 1) Даны два словаря: dictionary_1 = {'a': 300, 'b': 400} и dictionary_2 = {'c': 500, 'd': 600}.
# Объедините их в один при помощи встроенных функций языка Python. Результаты выведите на экран.

dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
merge_dict = dictionary_1.copy()
merge_dict.update(dictionary_2)
print(merge_dict)

merge_dict = {**dictionary_1, **dictionary_2}
print(merge_dict)

merge_dict = dictionary_1 | dictionary_2
print(merge_dict)

dictionary_1.update(dictionary_2)
print(dictionary_1)


# 2) Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран.
# Результаты выведите на экран.

dictionary = {1: 10, 2: 20, 3: 30}
x = 1
for val in dictionary.values():
    x *= val
print(x)


# 3) Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб.
# Результаты выведите на экран.

dictionary = {i: i**3 for i in range(1, 11)}
print(dictionary)

dictionary = {}
for i in range(1, 11):
    dictionary[i] = i**3
print(dictionary)


# 4) Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом,
# чтобы элементы первого списка были ключами, а элементы второго — соответственно значениями нашего словаря.
# Результаты выведите на экран.

list_1 = [1, 2, 3]
list_2 = [10, 20, 30]
dictionary = dict(zip(list_1, list_2))
print(dictionary)
