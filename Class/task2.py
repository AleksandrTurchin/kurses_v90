"""
Напишите программу с классом Math. Создайте два атрибута — a и b.
Напишите методы addition — сложение, multiplication — умножение, division — деление, subtraction — вычитание.
При вызове методов с параметрами a и b нужно производить соответствующие действия и печатать ответ.
"""

class ClassMath:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        if self.b != 0:
            return self.a / self.b
        else:
            print("Деление на ноль")

    def subtraction(self):
        return self.a - self.b


test = ClassMath(6, 3)
print(test.addition())
print(test.multiplication())
print(test.division())
print(test.subtraction())
