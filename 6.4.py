class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} стартует'

    def stop(self):
        return f'{self.name} останавливается'

    def turn_right(self):
        return f'{self.name} поворачивает на право'

    def turn_left(self):
        return f'{self.name} поворачивает на лево'

    def show_speed(self):
        return f'Скорость автомобиля: {self.name} составляет {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость городского автомобиля: {self.name} составляет {self.speed}')

        if self.speed > 40:
            return f'Скорость автомобиля: {self.name} выше разрешенной скорсти для городских авто'
        else:
            return f'Скорость автомобиля: {self.name} не превышает ограничение для городских авто'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость рабочего автомобиля: {self.name} составляет {self.speed}')

        if self.speed > 60:
            return f'Скорость автомобиля: {self.name} выше разрешенной скорсти для рабочих авто'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} из отделения полиции'
        else:
            return f'{self.name} не из отделения полиции'


bmw = SportCar(120, 'красная', 'BMW', False)
smart = TownCar(50, 'белая', 'Smart', False)
lada = WorkCar(90, 'черная', 'Lada', True)
skoda = PoliceCar(110, 'синия',  'Skoda', True)
print(lada.turn_left())
print(f'Когда {smart.turn_right()}, тогда {bmw.stop()}')
print(f'{lada.go()} со скоростью {lada.show_speed()}')
print(f'{lada.name}  {lada.color}')
print(f'{bmw.name} полицейская тачка? {bmw.is_police}')
print(f'{lada.name}  полицейская тачка? {lada.is_police}')
print(bmw.show_speed())
print(smart.show_speed())
print(skoda.police())
print(skoda.show_speed())