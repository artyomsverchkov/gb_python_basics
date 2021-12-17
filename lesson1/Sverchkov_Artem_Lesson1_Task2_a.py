# HW_Lesson1_Task2_a
# формирование списка нечетных чисел
my_list = []
i = 1
while i < 1000: # по условию список от 1 до 1000, 1000 - не входит
    my_list.append(i ** 3)
    i += 2
# print(my_list)
len_my_list = 'В списке {} элементов'.format(len(my_list))
# print(len_my_list)
# формирование нового списка из элментов кратных 7
new_list = []
new_sum = 0
for i in range(len(my_list)):
    dig_sum = 0
    dig_num = my_list[i]
    while (dig_num != 0):
        dig_sum = dig_sum + dig_num % 10
        dig_num = dig_num // 10
#    print(dig_sum)
    if dig_sum % 7 == 0:
        new_list.append(my_list[i])
        new_sum = new_sum + my_list[i]
        i += 1
    else:
        i += 1
len_new_list = 'В списке {} элемент(ов) кртных 7'.format(len(new_list))
# print(new_list)
# print(len_new_list)
result_sum = 'Сумма элементов списка кратных 7: {}'.format(new_sum)
print(result_sum)