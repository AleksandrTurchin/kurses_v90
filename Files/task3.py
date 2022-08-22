# 3)* Напишите программу, которая получает на вход строку с названием текстового файла,
# и выводит на экран содержимое этого файла, заменяя все запрещенные слова звездочками *
# (количество звездочек равно количеству букв в слове).
# Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле forbidden_words.txt.
# Все слова в этом файле записаны в нижнем регистре.
# Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова.
# Замена производится независимо от регистра: если файл forbidden_words.txt содержит запрещенное слово exam,
# то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.


with open('forbidden_words.txt', 'r', encoding='utf-8') as f:
	_tuple = tuple(f.read().split())
with open('test_for_task3.txt', 'r', encoding='utf-8') as f2:
	lower_to_f2 = f2.read().lower()
for i in _tuple:
	if i in lower_to_f2:
		change = '*' * len(i)
		lower_to_f2.replace(i, change)
print(lower_to_f2)


