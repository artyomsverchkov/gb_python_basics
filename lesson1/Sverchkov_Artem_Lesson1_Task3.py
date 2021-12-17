# HW_Lesson2_Task3
i = 1
my_list = ['процент', 'процента', 'процентов']
while i <= 100:
    if i // 10 < 1:
        if i == 1:
            result = '{} {}'.format(i, my_list[0])
            i += 1
            print(result)
        elif i in range(2, 5):
            result = '{} {}'.format(i, my_list[1])
            i += 1
            print(result)
        else:
            result = '{} {}'.format(i, my_list[2])
            i += 1
            print(result)
    elif i // 10 >= 1 and i // 10 < 2:
        result = '{} {}'.format(i, my_list[2])
        i += 1
        print(result)
    else:
        if i % 10 == 1:
            result = '{} {}'.format(i, my_list[0])
            i += 1
            print(result)
        elif i % 10 in range(2, 5):
            result = '{} {}'.format(i, my_list[1])
            i += 1
            print(result)
        else:
            result = '{} {}'.format(i, my_list[2])
            i += 1
            print(result)