# HW_Lesson2_Task2-3
# Решено для заданного списка
# Для input.list необходимы дополнительные условия (например: отрицательная температура)
my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result_my_list = 'Заданный список:\n{}'.format(my_list)
print(result_my_list)
len_my_list = 'Длина заданного списка: {} элементов\n'.format(len(my_list))
# print(len_my_list)
i = 0
while i < len(my_list):
    if my_list[i].isnumeric() and int(my_list[i]) < 10:
        my_list.insert(i, '"')
        my_list.insert(i + 1, '0' + str(int(my_list[i + 1])))
        my_list.pop(i + 2)
        my_list.insert(i + 2, '"')
        # print(my_list[i + 1])
        i += 3
    elif my_list[i].isnumeric() and int(my_list[i]) > 10:
        my_list.insert(i, '"')
        my_list.insert(i + 2, '"')
        # print(my_list[i + 1])
        i += 3
    else:
        try:
            int(my_list[i])
            my_list.insert(i, '"')
            my_list.insert(i + 1, '+0' + str(int(my_list[i + 1])))
            my_list.pop(i + 2)
            my_list.insert(i + 2, '"')
            # print(my_list[i + 1])
            i += 3
        except:
            # print(my_list[i])
            i += 1
result_list = 'Итоговый список:\n{}'.format(my_list)
print(result_list)

# result_as_str = ' '.join(my_list)
# print(result_as_str + '\n')
#
# print(len(my_list))

result = ""
i = 0
while i < len(my_list):
    if my_list[i] == '"':
        result = result + str(my_list[i]) + str(my_list[i + 1]) + str(my_list[i + 2]) + ' '
        # print(result)
        i += 3
    else:
        result = result + str(my_list[i]) + ' '
        i += 1
        # print(result)
result_str = 'Итоговая строка:\n{}'.format(result)
print(result_str)