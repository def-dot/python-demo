import datetime
import asyncio


a = [1] * 10000
b = [2] * 10000

def sync_t():
    time1 = datetime.datetime.now()
    for i in range(len(a)):
        print(a[i] + b[i])
    time2 = datetime.datetime.now()
    print((time2 - time1).microseconds)

async def print_t(i):
    print(a[i] + b[i])

def async_t():
    tasks = []
    for i in range(len(a)):
        tasks.append(print_t(i))
    loop = asyncio.get_event_loop()
    time1 = datetime.datetime.now()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    time2 = datetime.datetime.now()
    print((time2 - time1).microseconds)

async def coroutine_t(delay, message):
    await asyncio.sleep(delay)
    print(message)

async def exec_coroutine_t():
    t1 = datetime.datetime.now()
    await coroutine_t(1, "hello")
    await coroutine_t(2, "world")
    t2 = datetime.datetime.now()
    print("cost ", (t2-t1).seconds)

async def parallel_coroutine_t():
    t1 = datetime.datetime.now()
    task1 = asyncio.create_task(coroutine_t(1, "hello"))
    task2 = asyncio.create_task(coroutine_t(2, "world"))
    await task1
    await task2
    t2 = datetime.datetime.now()
    print("cost ", (t2 - t1).seconds)


if __name__ == '__main__':
    # async_t()
    # sync_t()
    asyncio.run(parallel_coroutine_t())
