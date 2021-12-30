# HW_Lesson5_Task1:
n = int(input('Введи n:\n'))


def numbers_gen(n):
    for numbers in range(n):
        yield numbers


print(*numbers_gen(n))
# print(type(numbers_gen))
