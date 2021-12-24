# HW_Lesson3_Task2
nl = '\n'
e_r_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
}


def num_translate_adv(e_word):
    if e_word[0] == e_word[0].upper():
        t_word = e_word.lower()
        return e_r_dict[t_word].capitalize()
    else:
        return e_r_dict[e_word]


e_word = input(f'Введи слово: {nl}')
translate_word = f'Перевод на русский:{nl}{num_translate_adv(e_word)}'
print(translate_word)