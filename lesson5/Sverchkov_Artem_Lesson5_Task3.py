# HW_Lesson5_Task3:
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
from itertools import zip_longest


def klass_gen():
    for tutor, klass in zip_longest(tutors, klasses):
        if tutors is not None:
            tuple_n = tutor, klass
        yield tuple_n


print(*klass_gen())
# print(type(klass_gen()))