# HW_Lesson5_Task5:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

new_src = []
for n in range(len(src)):
    if src.count(src[n]) == 1:
        new_src.append(src[n])
print(new_src)