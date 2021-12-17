# HW_Lesson1_Task2_b/с
# формирование списка нечетных чисел
my_list = []
i = 1
while i < 1000: # по условию список от 1 до 1000, 1000 - не входит
    my_list.append(i ** 3)
    i += 2
# print(my_list)
len_list = len(my_list)
# print(len_list)
# каждый элемент созданного списка увеличиваем на 17
for i in range(len(my_list)):
    my_list.append(my_list[0] + 17)
    del my_list[0]
print(my_list)
# проверка элементов списка кратных 7
result_sum = 0
i = 0
while i < len_list:
    # print(str(i) + ' . ' + str(my_list[i]))
# for i in range(len_list):
    dig_sum = 0
    dig_num = my_list[i]
    while (dig_num != 0):
        dig_sum = dig_sum + dig_num % 10
        dig_num = dig_num // 10
#    print(dig_sum)
    if dig_sum % 7 == 0:
        my_list.append(my_list[i])
        result_sum = result_sum + my_list[i]
        i += 1
    else:
        i += 1
del my_list[0:len_list]
len_list = 'В списке {} элемент(ов) кртных 7'.format(len(my_list))
print(my_list)
# print(len_list)
result = 'Сумма элементов списка кратных 7: {}'.format(result_sum)
print(result)
