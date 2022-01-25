# HW_Lesson9_Task2

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width


    def need_mass(self):
        mass = self._length * self._width * 25 * 5 / 1000
        return mass

road_size = Road(5, 10)
print(f'Необходимо асфальта {road_size.need_mass()} тонн')