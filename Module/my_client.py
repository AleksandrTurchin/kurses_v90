"""
Создайте второй модуль, my_client.py, который импортирует модуль my_mod и тестирует его функции.
"""

from Module.my_pkg.my_mod import count_lines, count_chars
print(count_lines('my_pkg/file.txt'), count_chars('my_pkg/file.txt'))
