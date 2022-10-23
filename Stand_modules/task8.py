"""
Отредактируйте предоставленную функцию, вызвав partial() и заменив первые три переменные в func().
Затем напечатайте с новой частичной функцией, используя только одну входную переменную, чтобы выход был равен 60.

from functools import partial
def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x

https://docs-python.ru/standart-library/modul-functools-python/funktsija-partial-modulja-functools/
"""

from functools import partial
def func(u, v, w, x):
    return u * 4 + v * 3 + w * 2 + x

partial_x = partial(func, 4, 5, 6)
print(partial_x(17))

#60