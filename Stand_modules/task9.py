"""
Напишите программу, чтобы создать итератор, который удаляет элементы из итерируемого объекта,
если элемент является положительным целым числом.

https://docs-python.ru/standart-library/modul-itertools-python/vvedenie-modul-itertools/
https://docs-python.ru/standart-library/modul-itertools-python/retsepty-ispolzovanija-modulja-itertools/
https://docs-python.ru/standart-library/modul-itertools-python/funktsija-filterfalse-modulja-itertools/
"""

from itertools import filterfalse


lst = [0, 2, 4, 12, -18, 13, 14, 22, 23, 44]
result = list(filterfalse(lambda x: x > 0, lst))
print(result)
