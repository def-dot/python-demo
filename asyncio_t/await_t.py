# await 可等待对象，支持协程、任务、Future
import asyncio


async def nested_t():
    return 1


async def coroutine_t():
    # coroutine_t()  # 会报错，coroutine was never awaited
    print(await nested_t())


async def task_t():
    task = asyncio.create_task(nested_t())
    print(await task)


async def future_t():
    task = asyncio.create_task(nested_t())
    print(await task)


# asyncio.run(coroutine_t())
asyncio.run(task_t())
