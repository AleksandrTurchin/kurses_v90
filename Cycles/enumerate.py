list = ('python')

for i, x in enumerate(list, 1):  # i - индекс, x - значение элемента
                                # list - итерируемый объект,
                                # 1 - начальное значение индекса (отcчет будет с единицы, т.к. по умолчанию 0)
    print(i, x)




a = [1, 4, 2, -5, 0, 11]

for i, x in enumerate(a):
    if x % 2 == 0:
        a[i] += 1

#print(a)

for i, x in enumerate(a):
    if x % 2 == 1:
        a[i] += 1

#print(a)

string = input()
symbol = input()

min_index, max_index = None, None

for i, v in enumerate(string):
     if v == symbol:
         if min_index is None:  # if Оператор может проверять условие в Python.
             # Чтобы проверить, является ли переменная None, мы можем использовать is ключевое слово.
             # Это ключевое слово проверяет, ссылаются ли две переменные на один и тот же объект.
             # https://www.delftstack.com/howto/python/check-if-variable-is-none-python/
                min_index = i
         max_index = i
print(min_index)
print(max_index)
