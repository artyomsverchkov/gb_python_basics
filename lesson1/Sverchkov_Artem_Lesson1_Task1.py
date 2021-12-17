# HW_Lesson1_Task1
duration = input('Введите количество секунд (type = int): ')

if duration.isnumeric():
    duration = int(duration)
    print(duration)

    if duration < 60:
        sec = '{} сек'.format(duration)
        print(sec)

    elif duration < 3600:
        min = duration // 60
        seс = duration % 60
        result = '{} мин {} сек'.format(min, seс)
        print(result)

    elif duration < 86400:
        hour = duration // 3600
        min = duration % 3600 // 60
        seс = duration % 3600 % 60
        result = '{} час {} мин {} сек'.format(hour, min, seс)
        print(result)

    else:
        day = duration // 86400
        hour = duration % 86400 // 3600
        min = duration % 86400 % 3600 // 60
        seс = duration % 86400 % 3600 % 60
        result = '{} дн {} час {} мин {} сек'.format(day, hour, min, seс)
        print(result)

else:
    print('Введеное значение не корректно')
