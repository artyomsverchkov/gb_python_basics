# HW_Lesson8_Task3

from functools import wraps
def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            print(f'{func.__name__}({arg}: {type(arg)})', end=', ')
        return func(*args)
    return wrapper


@type_logger
def calc_cube(*args):
    '''some function text'''
    return list(map(lambda x: x ** 3, args))


args = calc_cube(5, 4, 3)
print(args)