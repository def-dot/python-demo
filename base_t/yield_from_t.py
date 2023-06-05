# yield from 表示从什么地方生成，或者可以理解为委托什么什么生成
import asyncio


def yield_from_t():
    def gen():
        arr = [1, 2, 3]
        for i in arr:
            if i == 2:
                return i
            else:
                yield i

    def gen_from():
        # 生成器中return,只能通过捕获StopIteration异常实现
        # yield from 能够接收return值,而yield不能
        res = yield from gen()
        print("res %s" % res)

    print("yield ----------")
    for i in gen():
        print(i)

    print("yield from ----------")
    for i in gen_from():
        print(i)


@asyncio.coroutine
def async_1():
    print("async 1 starting...")
    yield from asyncio.sleep(5)
    print("async 1 end")
    return async_1.__name__


@asyncio.coroutine
def async_2():
    print("async 2 starting...")
    yield from asyncio.sleep(2)
    print("async 2 end")
    return async_2.__name__


@asyncio.coroutine
def async_wait():
    tasks = [async_1(), async_2()]
    # 等待所有任务执行完
    done, pending = yield from asyncio.wait(tasks)
    print("done %s" % done)
    print("pending %s" % pending)
    for i in done:
        print("res  %s" % i.result())


@asyncio.coroutine
def async_as_completed():
    tasks = [async_1(), async_2()]
    # as_completed 只要任一任务执行完，就输出
    for i in asyncio.as_completed(tasks):
        res = yield from i
        print("res %s" % res)


if __name__ == "__main__":
    yield_from_t()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_as_completed())
    loop.run_until_complete(async_wait())
    loop.close()


