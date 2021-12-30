# HW_Lesson5_Task4:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_src = []
for numbers in range(len(src) - 1):
    if src[numbers] < src[numbers + 1]:
        new_src.append(src[numbers + 1])
print(new_src)