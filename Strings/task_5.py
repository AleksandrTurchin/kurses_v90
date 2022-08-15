string = input('Введите строку: ')

revers_string = string[::-1]

if string == revers_string:
    print(string, 'является палиндромом')
else:
    print(string, 'не является палиндромом')
