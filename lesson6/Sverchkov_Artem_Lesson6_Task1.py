# HW_Lesson6_Task1
file = open('nginx_logs.txt', 'r', encoding='utf-8')
line = file.readline()
list_tuple = []
for line in file:
    ip = line[0:line.find(' - - ')]
    method = line[line.find(' "') + 2:line.find(' /')]
    link = line[line.find(' /') + 1:line.find(' HTTP/1.1"')]
    my_tuple = (ip, method, link)
    list_tuple.append(my_tuple)
file.close()
print(list_tuple)