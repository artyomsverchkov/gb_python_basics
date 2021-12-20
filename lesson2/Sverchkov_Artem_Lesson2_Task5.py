# HW_Lesson2_Task5
import decimal
nl = '\n'
my_list = [54.64, 546.5, 68.8, 78.3, 0.58, 98, 456.02, 786, 987.32, 156.59]
# print(f'Длина заданного списка: {len(my_list)} элементов')
print(f'Заданный список:{nl}{my_list}{nl}')


# Task 5_a
result_str_price = ''
for i in range(len(my_list)):
    str_price = format(my_list[i], '.2f')
    # print('str' + str(i + 1) + ': ' + str_price)
    # print('len_str' + str(i + 1) + ': ' + str(len(str_price)))
    a = 0
    if a in range(len(str_price)):
        # print('len_str: ' + str(len(str_price)))
        my_str = str(str_price)
        dot_num = my_str.find('.')
        len_str = len(my_str)
        true_price = ''
        if int(my_str[0:dot_num]) > 10:
            rub = my_str[0:dot_num]
            kk = my_str[dot_num+1:len_str]
            true_price = rub + ' руб ' + kk + ' коп'
            # result_str_price = result_str_price + rub + ' руб ' + kk + ' коп, '
        else:
            rub = '0' + my_str[0:dot_num]
            kk = my_str[dot_num + 1:len_str]
            true_price = rub + ' руб ' + kk + ' коп'
            # result_str_price = result_str_price + rub + ' руб ' + kk + ' коп, '
        if result_str_price == '':
            result_str_price = true_price
        else:
            result_str_price = result_str_price + ', ' + true_price
        # result_str_price = result_str_price + rub + ' руб ' + kk + ' коп, '
        # print(f'{rub} руб {kk} коп')
    else:
        print('!!!')

print(f'Task 5_a{nl}Итоговая строка:{nl}{result_str_price}')

#Task 5_b
print(f'{nl}Task 5_b{nl}Заданный список:{nl}{my_list}{nl}ID обекта "список": {id(my_list)}{nl}')
my_list.sort()
print(f'Отсортированный по возрастанию список:{nl}{my_list}{nl}ID обекта "список": {id(my_list)}')

#Task 5_с
print(f'{nl}Task 5_с{nl}Заданный список:{nl}{my_list}{nl}ID обекта "список": {id(my_list)}{nl}')
new_list = my_list.sort(reverse=True)
print(f'Отсортированный по убыванию список:{nl}{my_list}{nl}ID обекта "список": {id(new_list)}')

#Task 5_d
print(f'{nl}Task 5_d{nl}Отсортированный по убыванию список:{nl}{my_list}{nl}')
print(f'5 самых дорогих товаров:{nl}{my_list[0:5]}')