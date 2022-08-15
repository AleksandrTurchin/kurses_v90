string = input('Введите строку: ').lower()  # use lower() - convert to lowercase
symbol = input('Введите символ: ').lower()

if symbol in string:
    index1 = string.index(symbol)
    index2 = string.rindex(symbol)
    print('Индекс первого вхождения символа: ', index1)
    print('Индекс последнего вхождения символа: ', index2)
else:
    print('Такого символа нет в строке!')
