#  Пользователь вводит  строку и символ.
#  Необходимо определить индексы первого и последнего вхождения символа в строке, при этом нельзя использовать строковые методы для поиска.

string = input('Введите строку: ').lower()  # use lower() - convert to lowercase
symbol = input('Введите символ: ').lower()

counter = 0

for i, x in enumerate(string):
    if x == symbol:
        counter = 1
        break
if counter == 1:
    print(f'Индекс первого вхождения символа: {i}')

for i, x in enumerate(string[::-1]):
    if x == symbol:
        counter = 1
        break
if counter == 1:
    print(f'Индекс последнего вхождения символа: {len(string)-i + 1}')
    
if symbol not in string:
    print('Вхождений нет')
