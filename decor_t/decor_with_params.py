import datetime
import time


def cost(msg):
    def inner(func):
        def wrapper(*args, **kwargs):
            time1 = datetime.datetime.now()
            func()
            time2 = datetime.datetime.now()
            print((time2-time1).seconds, msg)
        return wrapper
    return inner


@cost(msg='test')
def hello():
    print('hello')
    time.sleep(5)


hello()
