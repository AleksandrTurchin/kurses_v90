number_month = int(input('Введите номер месяца: '))

if number_month in (1, 2, 12):
    print('Это Зима')
elif number_month in (3, 4, 5):
    print('Это Весна')
elif number_month in (6, 7, 8):
    print('Это Лето')
elif number_month in (9, 10, 11):
    print('Это Осень')
else:
    print('Неправильно указан номер месяца, укажите от 1 до 12: ')
