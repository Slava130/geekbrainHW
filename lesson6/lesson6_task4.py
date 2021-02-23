# . Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
class Car:
    speed = None
    color=None
    name=None
    is_police = False

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = True if is_police else False
    def go(self):
        return f'Машина двигается'
    def stop(self):
        return f'Машина остановилась'
    def turn(self,direction):
        return print(f'Машина поворачивает' + direction)

    def show_speed(self):
        return f'Скорость', self.name , self.speed

class TownCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)

    def show_speed(self):
        print('Скорость', self.name , self.speed)

        if self.speed > 60:
            return 'Скорость превышена'
        else:
            return 'Скорось нормальная'
class SportCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)

class WorkCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color,is_police)
    def show_speed(self):
        print('Скорость', self.name , self.speed)

        if self.speed > 40:
            return 'Скорость превышена'
        else:
            return 'Скорось нормальная'
class PoliceCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)



zaz = TownCar('Zaz',30, 'Black')
mersedes = SportCar('Marsedes Benz', 100, 'White')
gaz = WorkCar('Gaz', 70, 'Green', True)
maserati = PoliceCar('Maserati', 110, 'Blue', True)
print(mersedes.show_speed())
print(gaz.show_speed())
print(zaz.is_police)
print (maserati.name,maserati.turn(left))