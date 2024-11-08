import asyncio


async def nested(name, seconds):
    await asyncio.sleep(seconds)
    return name


async def main():
    task1 = asyncio.create_task(nested("A", 1))
    task2 = asyncio.create_task(nested("B", 2))

    # 等待任意一个任务完成
    done, pending = await asyncio.wait({task1, task2}, return_when=asyncio.FIRST_COMPLETED)

    # 处理已完成的任务
    for task in done:
        print(f"{task.result()} is done")

    # 取消未完成的任务
    for task in pending:
        print(f"{task} is pending")
        task.cancel()


asyncio.run(main())
