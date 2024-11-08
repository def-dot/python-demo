import time


def cost(func):
    # 函数方式定义装饰器
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("cost %s" % (end-start))
    return wrapper


class Cost:
    # 类方式定义装饰器
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        res = self.func(*args, **kwargs)
        end = time.time()
        print("cost %s" % (end - start))
        return res


@cost
def calc_t():
    sum = 0
    for i in range(1000):
        sum += i
    return sum


if __name__ == "__main__":
    calc_t()
