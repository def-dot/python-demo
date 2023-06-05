def next_t():
    def gen():
        # 测试next send
        while True:
            res = yield 4
            print("res %s" % res)

    # next执行，send传递参数执行
    g = gen()
    print(g)
    print("next 1-----")
    print(next(g))
    print("next 2-------")
    print(next(g))
    print("next 3-------")
    print(g.send(3))


def for_t():
    def gen_for():
        # 测试循环
        for i in range(5):
            res = yield i
            print("res %s" % res)

    # for会自动调用next执行，循环结束不会抛出异常
    g = gen_for()
    for i in g:
        print(i)


def end_t():
    # 测试结束
    def gen_end():
        res = yield 4
        print("res %s" % res)

    # 生成器结束后抛出StopIteration异常
    g = gen_end()
    print("next 1-----")
    print(next(g))
    print("next 2-----")
    print(next(g))


def return_t():
    def gen_return():
        for i in range(5):
            if i == 2:
                return i
            else:
                yield i

    # 不能获取return的值, return的值要靠StopIteration捕获，但是for循环不会显示抛出终止异常，所以不能获取return的值。若要获取return的值，需要一步一步调用next，并捕获StopIteration异常来获得。
    for i in gen_return():
        print(i)


if __name__ == "__main__":
    next_t()
    # for_t()
    # end_t()
    # return_t()
