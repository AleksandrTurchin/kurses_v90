# Напишите функцию, чтобы проверить, является ли строка панграммой или нет.
# Панграмма — фраза, содержащая в себе все буквы алфавита.

def test_pangrama(text):
    return not (set('abcdefghijklmnopqrstuvwxyz') - set(text.lower()))

# Тесты
print(test_pangrama('The quick brown fox jumps over the lazy dog'))
print(test_pangrama('I love python'))



