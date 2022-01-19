# HW_Lesson8_Task1
import re
regex = re.compile(r'(^[a-zA-Z0-9._-]{5,})@([a-zA-Z.]+\.[a-zA-Z]{2,}$)')


def email_parse(email_address):
    found_info = regex.findall(email_address)
    if found_info:
        email_name, email_service = found_info[0]
    else:
        raise ValueError(f'Не корректный адрес email')
    email_dict = {'username': email_name, 'domain': email_service}
    return print(email_dict)


user_email = input('Введите email: \n')
email_parse(user_email)