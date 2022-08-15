string = input('Введите строку: ').lower()  # use lower() - convert to lowercase
symbol = input('Введите символ: ').lower()

number_occurrences = string.count(symbol)  # use count()

print('Количество символов в строке: ', number_occurrences)
