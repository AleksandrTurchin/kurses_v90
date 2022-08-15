#  Пользователь вводит строку и символ.
#  Определить количество вхождений символа в строку, независимо от регистра, при этом нельзя использовать метод count.

string = input('Введите строку: ').lower()  # use lower() - convert to lowercase
symbol = input('Введите символ: ').lower()

counter = 0

for i in string:
    if i == symbol:
        counter += 1
print(f'Количесвто вхождений в символа в строку: {counter}')
