import asyncio
import signal


async def test1():
    # 状态通知
    async def db(db_set: asyncio.Event):
        print("启动数据库...")
        await asyncio.sleep(3)
        print("数据库启动完成！")
        db_set.set()

    async def redis(redis_set: asyncio.Event):
        print("启动Redis...")
        await asyncio.sleep(2)
        print("Redis启动完成！")
        redis_set.set()

    async def api(db_set, redis_set):
        print("启动API...")
        await db_set.wait()
        await redis_set.wait()
        print("API启动完成！")

    db_set = asyncio.Event()
    redis_set = asyncio.Event()
    await asyncio.gather(
        db(db_set),
        redis(redis_set),
        api(db_set, redis_set),
    )


async def test2():
    # 优雅停机
    stop_event = asyncio.Event()

    async def worker(name: str, stop_event: asyncio.Event):
        print(f"Worker {name} 启动")
        while not stop_event.is_set():
            print(f"Worker {name} 正在工作...")
            await asyncio.sleep(1)
        print(f"Worker {name} 收到停止信号，正在清理资源...")
        await asyncio.sleep(2)
        print(f"Worker {name}已停止")

    loop = asyncio.get_running_loop()

    # On Windows, SIGTERM and SIGHUP are not available, so we only handle SIGINT
    try:
        loop.add_signal_handler(signal.SIGINT, signal_handler)
        if hasattr(signal, 'SIGTERM'):
            loop.add_signal_handler(signal.SIGTERM, signal_handler)
    except NotImplementedError:
        # On Windows, signal handling is limited, so we'll use a keyboard interrupt handler
        print("信号处理在此平台上不受支持，使用键盘中断 (Ctrl+C) 来停止程序")

    tasks = [
        asyncio.create_task(worker("worker 1", stop_event)),
        asyncio.create_task(worker("worker 2", stop_event)),
    ]

    # Wait for stop event to be set
    while not stop_event.is_set():
        await asyncio.sleep(0.1)

    # Wait for all tasks to complete
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    # asyncio.run(test1())
    asyncio.run(test2())
