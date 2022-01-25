# HW_Lesson9_Task5

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Начало отрисовки')


class Pen(Stationary):
    def draw(self):
        print('Ручка пишет')

class Pencil(Stationary):
    def draw(self):
        print('Карандаш пишет')

class Handle(Stationary):
    def draw(self):
        print('Маркер рисует')

pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

pen.draw()
pencil.draw()
handle.draw()