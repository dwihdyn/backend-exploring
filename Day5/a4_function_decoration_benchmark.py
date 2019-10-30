# this sample is given during the lecture - nicholas

from time import time, sleep


def timer(func):
    def wrapper():
        x = time()
        func()
        y = time()
        print(y - x)
    return wrapper


@timer
def a():
    sleep(1)


@timer
def b():
    sleep(2)


a()
b()
