"""
Напишите функцию для создания строки HTML с тегами вокруг слов (использовать шаблону из модуля string).
Пример функции и результата:
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'

https://www.geeksforgeeks.org/template-class-in-python/
"""

from string import Template

def add_tags(tag, word):
	v = {'tag': tag, 'word': word}
	s = Template('<$tag>$word</$tag>')
	return s.substitute(v)                              # f'<{tag}>{word}</{tag}>'

# tests
print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))
