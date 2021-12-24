# HW_Lesson3_Task3
names = ["Иван", "Мария", "Петр", "Илья"]


def thesaurus(names):
    my_dict = {}
    for i in range(len(names)):
        f_word = names[i]
        key = f_word[0]
        value = names[i]
        # print(key)
        # print(value)
        my_dict.setdefault(key, [])
        my_dict[key].append(value)
    return my_dict


print(thesaurus(names))