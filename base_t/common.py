import time


def cost(func):
    # 耗时时间装饰器
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("cost %s" % (end-start))
    return wrapper
