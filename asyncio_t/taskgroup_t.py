import asyncio


async def task1():
    await asyncio.sleep(1)
    print(1)
    return 1


async def task2():
    print(2)
    raise Exception("error")  # taskgroup中一个任务异常，其他任务会取消
    return 2


async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(task1())
            tg.create_task(task2())
    except Exception as e:
        pass

    await asyncio.sleep(2)
    print("main-------")


asyncio.run(main())
