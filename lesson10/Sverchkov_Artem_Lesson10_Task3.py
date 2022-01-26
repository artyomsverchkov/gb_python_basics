# HW_Lesson10_Task3
class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for i in range(self.nums // rows)]) \
               + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return str(self.nums)

    def __add__(self, other):
        return 'Сумма клеток: ' + str(self.nums + other.nums)

    def __sub__(self, other):
        return self.nums - other.nums if self.nums - other.nums > 0 \
            else 'Ячеек в первой клетке меньше или равно второй, вычитание невозможно'

    def __mul__(self, other):
        return 'Умножение клеток: ' + str(self.nums * other.nums)

    def __truediv__(self, other):
        return 'Деление клеток: ' + str(round(self.nums / other.nums))


cell_1 = Cell(15)
cell_2 = Cell(53)
print(cell_1)
print(cell_1 + cell_2)
print(cell_1.make_order(10))