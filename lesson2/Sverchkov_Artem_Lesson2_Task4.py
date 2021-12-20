# HW_Lesson2_Task4
my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result_list = 'Заданный список:\n{}\n'.format(my_list)
print(result_list)

for i in range(len(my_list)):
    if i in range(len(my_list[i])):
        my_str = my_list[i]
        last_space = my_str.rfind(' ')
        # print('пробел: ' + str(last_space))
        len_str = len(my_str)
        name = my_str[last_space + 1:len_str]
        result = 'Привет, {}!'.format(name.capitalize())
        print(result)