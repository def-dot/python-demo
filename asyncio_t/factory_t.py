import asyncio


async def nested():
    return 1


async def main():
    loop = asyncio.get_running_loop()
    loop.set_task_factory(asyncio.eager_task_factory)  # 设置事件循环使用eager_task_factory， 任务会立即执行，而不是等待事件循环定时调用

    task1 = loop.create_task(nested())
    task2 = loop.create_task(nested())

    results = await asyncio.gather(task1, task2)
    print(results)


asyncio.run(main())
