import asyncio
import datetime


async def delay(seconds, text):
    await asyncio.sleep(seconds)
    print(text)


async def create_task_t():
    task1 = asyncio.create_task(delay(1, "hello"))  # 创建并发任务
    task2 = asyncio.create_task(delay(2, "world"))
    print(f"start {datetime.datetime.now()}")
    await task1  # 执行task1，task2，并等待任务执行完毕
    await task2
    print(f"end {datetime.datetime.now()}")


async def taskgroup_t():
    async with asyncio.TaskGroup() as tg:  # 3.11 引入
        tg.create_task(delay(1, "hello"))
        tg.create_task(delay(2, "world"))
        print(f"start {datetime.datetime.now()}")
    print(f"end {datetime.datetime.now()}")


# asyncio.run(create_task_t())
asyncio.run(taskgroup_t())
