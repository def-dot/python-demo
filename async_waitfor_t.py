import asyncio

async def my_task():
    # 模拟一个耗时 5 秒的操作
    await asyncio.sleep(5)
    return "任务完成"

async def main():
    try:
        # 设置超时时间为 2 秒
        result = await asyncio.wait_for(my_task(), timeout=2.0)
        print(result)
    except asyncio.TimeoutError:
        print("太慢了，任务超时！")

asyncio.run(main())