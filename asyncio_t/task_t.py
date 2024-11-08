import asyncio


async def nested(second):
    await asyncio.sleep(second)
    return 1


def callback(task):
    print("over", task.result())


async def main():
    t = asyncio.create_task(nested(1))
    t.add_done_callback(callback)  # 完成后回调，参数只能是一个普通函数（带一个默认参数，接收task对象本身，不能是协程）
    # print(type(t))  # asyncio.Task对象
    # print(isinstance(t, asyncio.Future))  # Task是Future的子类
    # print(t.done())
    # print(t.result())
    print(t.get_stack())
    print(t.get_coro())
    r = await t
    print("main", r)

asyncio.run(main())
