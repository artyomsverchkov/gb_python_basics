# HW_Lesson6_Task3
from itertools import zip_longest
import json
out_dict = {}
with open('users.csv', encoding='utf-8') as users, open('hobby.csv', encoding='utf-8') as hobby:
    users_n_lines = 0
    for line in users:
       users_n_lines += 1
    hobby_n_lines = 0
    for line in hobby:
        hobby_n_lines += 1
    if users_n_lines < hobby_n_lines:
        exit(1)
    users.seek(0)
    hobby.seek(0)
    for line_user, line_user_hobby in zip_longest(users, hobby):
        if line_user_hobby is not None:
            out_dict[line_user.strip()] = line_user_hobby.strip()
        else:
            hobby_n_lines
with open('dict.json', 'w', encoding='utf-8') as file:
    json.dump(out_dict, file)
print(out_dict)