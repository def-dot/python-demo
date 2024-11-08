import asyncio


async def nested():
    print(1)
    await asyncio.sleep(5)
    print(2)
    return 2


async def main():
    task = asyncio.create_task(nested())
    shield_task = asyncio.shield(task)   # asyncio.shield后，cancel不生效了，协程还能执行

    await asyncio.sleep(1)
    shield_task.cancel()  # 取消协程

    await shield_task
    return 1


asyncio.run(main())
