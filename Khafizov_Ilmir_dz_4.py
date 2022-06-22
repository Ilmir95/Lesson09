class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(f'{self.name} поехала')
    def stop(self):
        print(f'{self.name} остановилась')
    def turn(self, direction):
        print(f'{self.name} повернула {direction}')
    def show_speed(self):
        print('Текущая скорость: ', self.speed)

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Внимание превышение скорости')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Внимание превышение скорости')

class PoliceCar(Car):
    pass

town_car = TownCar(90, 'Белая', 'Lada', False)
sport_car = SportCar(320, 'Синия', 'Ferrari', False)
work_car = WorkCar(70, 'Черная', 'BMW', False)
police_car = PoliceCar(210, 'Хаки', 'Tesla', True)

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.turn('Влево')