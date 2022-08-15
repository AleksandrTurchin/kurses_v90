WINTER_MONTH_NUMBER = (1, 2, 12)
SPRING_MONTH_NUMBER = (3, 4, 5)
SUMMER_MONTH_NUMBER = (6, 7, 8)
AUTUMN_MONTH_NUMBER = (9, 10, 11)

number_month = int(input('Введите номер месяца: '))

if number_month in WINTER_MONTH_NUMBER:
    print('Это Зима')
elif number_month in SPRING_MONTH_NUMBER:
    print('Это Весна')
elif number_month in SUMMER_MONTH_NUMBER:
    print('Это Лето')
elif number_month in AUTUMN_MONTH_NUMBER:
    print('Это Осень')
else:
    print('Неправильно указан номер месяца, укажите от 1 до 12: ')
