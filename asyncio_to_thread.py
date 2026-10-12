import asyncio
import time

async def my_task():
    print("准备外包...")
    result = await asyncio.to_thread(sync_blocking_work) 
    print("外包干完了，结果是:", result)

def sync_blocking_work():
    print("sync 干活中...")
    time.sleep(5)
    print("sync 干完活了")


asyncio.run(my_task())