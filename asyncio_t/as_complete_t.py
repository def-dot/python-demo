import asyncio

async def my_task(name, delay):
    await asyncio.sleep(delay)
    print(f"任务 {name} 完成")
    return f"结果来自 {name}"

async def main():
    tasks = [
        my_task("A", 5),
        my_task("B", 1)
    ]

    # 使用 as_completed 获取任务完成的顺序
    for coro in asyncio.as_completed(tasks):
        result = await coro  # 等待下一个任务完成
        print(result)  # 输出完成任务的结果

# 运行事件循环
asyncio.run(main())
