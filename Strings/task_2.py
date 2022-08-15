str1 = input('Введите строку 1: ')
str2 = input('Введите строку 2: ')

# use sorted() - pythonru.com/osnovy/vozmozhnosti-i-primery-funkcii-sorted-v-python
sorted_str1 = sorted(str1)
sorted_str2 = sorted(str2)

if sorted_str1 == sorted_str2:
    print(f'{str1} и {str2} являются анаграмой.')
else:
    print(f'{str1} и {str2} не являются анаграмой.')
