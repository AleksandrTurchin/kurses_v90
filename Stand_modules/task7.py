"""
Напишите программу для поиска наиболее распространенных элементов и их количества в указанном тексте.

https://docs-python.ru/standart-library/modul-collections-python/klass-counter-modulja-collections/
"""

from collections import Counter
text = input('Input our text for test: ').lower().split()
result = Counter(text).most_common(5)
print(dict(result))
