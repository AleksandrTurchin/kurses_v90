"""
Напишите игру в кости.

https://docs-python.ru/standart-library/modul-random-python/sluchajnye-tselye-chisla-modulja-random/
https://docs-python.ru/standart-library/modul-sys-python/funktsija-exit-modulja-sys/
"""

import sys
from random import randint

print('Добро пожаловать в игру "Кости". Правила просты: бросаем пару костей, у кого результат больше тот и выиграл')
answer = input('Играем? (Напиши ответ: Да или Нет): ')

if answer.lower() == 'да':
    print('Тогда начнем игру!')
else:
    print('Пока! Заходи еще!')
    sys.exit()

player_one = input('Введите имя игрока 1:  ')
player_two = input('Введите имя игрока 2:  ')

input('{} нажмите клавишу enter, чтобы бросить кости'.format(player_one))

dice1_player_one = randint(1, 6)
dice2_player_one = randint(1, 6)
sum_dices_player_one = dice1_player_one + dice2_player_one

print('У игрока {} значение 1-ого кубика {}, значение 2-ого кубика {}, сумма двух кубиков {}'.format(player_one, dice1_player_one, dice2_player_one, sum_dices_player_one))

input('{} нажмите клавишу enter, чтобы бросить кости'.format(player_two))

dice1_player_two = randint(1, 6)
dice2_player_two = randint(1, 6)
sum_dices_player_two = dice1_player_two + dice2_player_two

print('У игрока {} значение 1-ого кубика {}, значение 2-ого кубика {}, сумма двух кубиков {}'.format(player_two, dice1_player_two, dice2_player_two, sum_dices_player_two))

if sum_dices_player_one > sum_dices_player_two:
    print('Игрок {} выиграл! Поздравляем!!'.format(player_one))
elif sum_dices_player_one < sum_dices_player_two:
    print('Игрок {} выиграл! Поздравляем!!'.format(player_two))
else:
    print('Ничья! Победила дружба!! :)')
