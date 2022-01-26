# HW_Lesson10_Task1
class Matrix:
    def __init__(self, input_data):
        self.input = input_data

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.input])

    def __add__(self, other):
        result = ''
        if len(self.input) == len(other.input):
            for line_1, line_2 in zip(self.input, other.input):
                if len(line_1) != len(line_2):
                    return 'Сложение невозможно! Размер первой матрицы не соответствует размеру второй (горизонталь)'

                summed_line = [x + y for x, y in zip(line_1, line_2)]
                result += ' '.join(map(str, summed_line)) + '\n'
        else:
            return 'Сложение невозможно! Размер первой матрицы не соответствует размеру второй (вертикаль)'
        return result


matrix_1 = Matrix([[31, 22], [37, 43], [51, 86]])
matrix_2 = Matrix([[3, 8], [5, 3], [8, 7]])
print(matrix_1, '\n')
print(matrix_2, '\n')
print(matrix_1 + matrix_2)