# 函数重写
import contextlib


def with_t():
    # with 上下文，使用with关键字，进入with最先做什么（__enter__），推出with最后要做什么（__exit__）
    class Query:
        def __enter__(self):
            print("__enter__")
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            print("__exit__")

        def query(self):
            return "query !!"

    # with Query() as q:
    # q = Query()
    # r = q.query()
    # print(r)

    with Query() as q:
        r = q.query()
        print(r)


def gen_t():
    # 生成器的方式
    class Query:
        def query(self):
            return "query !!"

    def create_query():
        print("__enter__")
        q = Query()
        yield q
        print("__exit__")

    g = create_query()
    q = next(g)
    r = q.query()
    print(r)
    next(g)


def context_t():
    # 上下文
    class Query:
        def query(self):
            return "query !!"

    @contextlib.contextmanager
    def create_query():
        print("__enter__")
        q = Query()
        yield q
        print("__exit__")

    with create_query() as q:
        r = q.query()
        print(r)


def decor_t():
    # 装饰器，函数重写
    def myfunc(func):
        def wrapper(*args, **kwargs):
            print('__enter__')
            res = func(*args, **kwargs)
            print('__exit__')
            return res
        return wrapper

    class Query:
        @myfunc
        def query(self):
            return "query !!"

    q = Query()
    r = q.query()
    print(r)


def for_t():
    # with的__exit__不管什么时候都会执行
    @contextlib.contextmanager
    def test():
        print("__enter__")
        yield
        print('__exit__')

    a = 0
    while True:
        a += 1
        with test() as t:
            print(f"a is {a}")
            if a % 2 == 0:
                break


if __name__ == '__main__':
    for_t()
    # with_t()
    # decor_t()
    # gen_t()
    # context_t()
