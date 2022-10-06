"""
Напишите программу Python для отображения календаря для в заданной локали. (модуль calendar)
https://docs-python.ru/standart-library/modul-calendar-python/tekstovyj-html-kalendari-russkom-jazyke/
https://docs-python.ru/standart-library/modul-calendar-python/funktsii-atributy-modulja-calendar/
https://tonais.ru/osnovy/modul-calendar-v-python
"""

import calendar
c = calendar.LocaleTextCalendar(locale='en_US.UTF-8')
print(c.prmonth(2022, 10))

# print(c.formatmonth(2022, 10))
