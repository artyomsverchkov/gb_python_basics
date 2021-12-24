# HW_Lesson3_Task4
names_surnames = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"]


def thesaurus(names_surnames):
    my_dict = {}
    for i in range(len(names_surnames)):
        word_pair = names_surnames[i].split(' ')
        surname = word_pair[1]
        surname_key = surname[0]
        name = word_pair[0]
        name_key = name[0]
        my_dict.setdefault(surname_key, {})
        my_dict[surname_key].setdefault(name_key, [])
        my_dict[surname_key][name_key].append(word_pair)
    return my_dict


print(thesaurus(names_surnames))