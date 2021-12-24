# HW_Lesson3_Task1
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


def num_translate(e_word):
    return e_r_dict.get(e_word)


e_word = input(f'Введи слово: {nl}')
translate_word = f'Перевод на русский:{nl}{num_translate(e_word)}'
print(translate_word)