"""
??????????
Напишите скрипт для отображения различных форматов даты и времени.
а) Текущая дата и время
б) Текущий год
в) Месяц года
г) номер недели в году
д) будний день недели
е) День года
г) день месяца
з) День недели
"""

import time
import datetime
print("Текущая дата и время: " , datetime.datetime.now())
print("Текущий год: ", datetime.date.today().strftime("%Y"))
print("Месяц года: ", datetime.date.today().strftime("%B"))
print("номер недели в году: ", datetime.date.today().strftime("%W"))
print("будний день недели: ", datetime.date.today().strftime("%w"))
print("День года: ", datetime.date.today().strftime("%j"))
print("день месяца : ", datetime.date.today().strftime("%d"))
print("День недели: ", datetime.date.today().strftime("%A"))
