n = int(input('Введите трехзначное число n = '))

a = n % 10  # первый символ трехзначного числа
b = n % 100 // 10  # второй символ трехзначного числа
c = n // 100  # первый символ трехзначного числа

result = (a + b + c)

print("Сумма цифр трехзначного числа будет равна: ", result)
