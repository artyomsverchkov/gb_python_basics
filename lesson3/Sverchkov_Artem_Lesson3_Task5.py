# HW_Lesson3_Task5
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
jokes_num = int(input(f'Введите количество шуток:\n'))
repits = input(f'Укажите возможность повторений слов в шутках [y/n]:\n')


def get_jokes(repits, jokes_num):
    random.shuffle(nouns)
    random.shuffle(adverbs)
    random.shuffle(adjectives)
    jokes_list = []
    if repits == 'n' and jokes_num <= min(len(nouns), len(adverbs), len(adjectives)):
        for i in range(jokes_num):
            jokes_list.append(f'{nouns[i]} {adverbs[i]} {adjectives[i]}')
    elif repits == 'n' and jokes_num > min(len(nouns), len(adverbs), len(adjectives)):
        print(f'Максимальное количество шуток без повторений слов: {max(len(nouns), len(adverbs), len(adjectives))} \n'
              f'полный список уникальных шуток:')
        for i in range(min(len(nouns), len(adverbs), len(adjectives))):
            jokes_list.append(f'{nouns[i]} {adverbs[i]} {adjectives[i]}')
    else:
        for i in range(jokes_num):
            random.shuffle(nouns)
            random.shuffle(adverbs)
            random.shuffle(adjectives)
            jokes_list.append(f'{nouns[0]} {adverbs[0]} {adjectives[0]}')
    return jokes_list


result_jokes = get_jokes(repits, jokes_num)
for i in range(len(result_jokes)):
    print(result_jokes[i])