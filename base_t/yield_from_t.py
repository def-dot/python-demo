# yield from 表示从什么地方生成，或者可以理解为委托什么什么生成
import asyncio


def gen_from_iter():
    # 从迭代器生成,，如数组、元组、字典等
    arr = [1, 2, 3]
    yield from arr


def gen():
    arr = [1, 2, 3]
    for i in arr:
        yield i


def gen_return():
    for i in range(5):
        if i == 2:
            return i
        else:
            yield i


def gen_from_gen():
    # 从生成器生成，和直接从生成器生成没啥区别
    yield from gen()


def yield_from_return_t():
    # 通过yield from接收return值
    res = yield from gen_return()
    print("res %s" % res)


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


@asyncio.coroutine
def async_main():
    # 协程中没有yield，不会报错
    # yield from async_wait()
    yield from async_as_completed()


@asyncio.coroutine
def async_coroutine_t():
    # yield from async_wait()
    return 1


if __name__ == "__main__":
    # for i in gen():
    #     print(i)
    # for i in gen_from_gen():
    #     print(i)

    # for i in yield_from_return_t():
    #     print(i)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_main())
    loop.close()
