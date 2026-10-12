import asyncio


def test_lock():
    # 创建一个全局锁
    lock = asyncio.Lock()
    shared_resource = 0

    async def update_resource():
        nonlocal shared_resource
        
        # 获取锁
        async with lock:
            print(f"正在处理资源...")
            current_value = shared_resource
            await asyncio.sleep(1)
            shared_resource = current_value + 1

    async def main():
        # 同时运行多个协程
        await asyncio.gather(update_resource(), update_resource())
        print(f"最终结果: {shared_resource}")

    asyncio.run(main())



def test_semaphore():
    # 创建一个信号量，允许最多2个协程同时访问
    semaphore = asyncio.Semaphore(2)
    shared_resource = 0

    async def update_resource():
        nonlocal shared_resource
        
        # 获取信号量
        async with semaphore:
            print(f"正在处理资源...")
            current_value = shared_resource
            await asyncio.sleep(1)
            shared_resource = current_value + 1

    async def main():
        # 同时运行多个协程
        await asyncio.gather(update_resource(), update_resource(), update_resource())
        print(f"最终结果: {shared_resource}")

    asyncio.run(main())



if __name__ == "__main__":
    # test_lock()
    test_semaphore()
