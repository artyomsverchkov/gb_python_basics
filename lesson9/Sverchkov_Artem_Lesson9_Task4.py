# HW_Lesson9_Task4

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        print(f'{self.name} продолжает движение')

    def stop(self):
        print(f'{self.name} останавливается')

    def turn(self, direction):
        print(f'{self.name} направление движения {direction}')

    def show_speed(self):
        print(f'Скорость: {self.speed}')



class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Ваша скорость больше разрешенной!')


class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        print(f'Скорость {self.speed}')
        if self.speed > 40:
            print(f'Ваша скорость больше разрешенной!')

class PoliceCar(Car):
    pass


sport_car = SportCar(278, 'Зеленый', 'Спортивный автомобиль', False)
town_car = TownCar(125, 'Черный', 'Городской автомобиль', False)
work_car = WorkCar(90, 'Рыжий', 'Рабочая автомобиль', False)
police_car = PoliceCar(190, 'Синий', 'Полицейский автомобиль', True)

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.turn('Правый поворот')
