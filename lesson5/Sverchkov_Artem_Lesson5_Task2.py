# HW_Lesson5_Task2:
n = int(input('Введи n:\n'))
nums_gen = (numbers for numbers in range(n))
print(*nums_gen)
# print(type(nums_gen))