# HW_Lesson6_Task2
with open('nginx_logs.txt') as file:
    data = []
    result_dict = {}
    for line in file:
        ip = line[0:line.find(' - - ')]
        result_dict.setdefault(ip, 0)
        result_dict[ip] += 1
ip_max_count = max(result_dict, key=lambda x: result_dict[x])
# print(my_dict)
print(f'IP адрес спамера: {ip_max_count}\nКоличество запросов: {result_dict[ip_max_count]}')