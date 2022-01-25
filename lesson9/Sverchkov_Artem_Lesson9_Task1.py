# HW_Lesson9_Task1

from itertools import cycle
from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = (('красный', 5), ('желтый', 2), ('зеленый', 5))

    def running(self):
        for color, sec in cycle(self.__color):
            print(f'Цвет светофора {color}, ожидайте {sec} секунд')
            sleep(sec)


traffic_light = TrafficLight()
traffic_light.running()