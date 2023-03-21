import datetime
import time


def cost(func):
    def wrapper(*args, **kwargs):
        time1 = datetime.datetime.now()
        func()
        time2 = datetime.datetime.now()
        print((time2-time1).seconds)
    return wrapper


@cost
def hello():
    print('hello')
    time.sleep(5)


hello()
