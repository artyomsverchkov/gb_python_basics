# HW_Lesson6_Task4
from itertools import zip_longest
with open('users_hobby.txt', 'w', encoding='utf-8') as file, open('users.csv', encoding='utf-8') as users,\
        open('hobby.csv', encoding='utf-8') as hobby:
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
                    file.write(f'{line_user.strip()}: {line_user_hobby.strip()}\n')
                else:
                    file.write(f'{line_user_hobby}\n')