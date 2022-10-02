"""
Напишите программу с классом Car. Создайте инициализатор класса Car.
Создайте атрибуты класса Car — color (цвет), type (тип), year (год).
Напишите пять методов.
Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
Третий — присвоение автомобилю года выпуска.
Четвертый метод — присвоение автомобилю типа.
Пятый — присвоение автомобилю цвета.
"""

class Car:

    def __init__(self, color, cartype, year):
        self.color = color
        self.cartype = cartype
        self.year = year

    def engine_on(self):
        print('Автомобиль заведен')

    def engine_off(self):
        print('Автомобиль заглушен')

    def car_year(self, year):
        self.year = year

    def car_type(self, cartype):
        self.cartype = cartype

    def car_color(self, color):
        self.color = color

car = Car('red', 'sedan', '2017')
print(car.__dict__)
car.engine_on()
car.engine_off()

car.car_year(2002)
car.car_color('blue')
car.car_type('Coupe')
print(car.__dict__)
