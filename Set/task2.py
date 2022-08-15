# Даны два списка чисел, которые могут содержать до 10000 чисел каждый.
# Выведите все числа, которые входят как в первый, так и во второй список в порядке возрастания.


list_1 = input('Введите числа в список 1 через запятую: ')
list_2 = input('Введите числа в список 2 через запятую: ')

set_1 = set(list_1.split(','))
set_2 = set(list_2.split(','))

set_all = set_1.intersection(set_2)
print(sorted(set_all))

