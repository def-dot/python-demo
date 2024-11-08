import asyncio
import datetime
import time


def block_t():
    time.sleep(1)


async def main():
    print("start", datetime.datetime.now())
    await asyncio.gather(
        asyncio.to_thread(block_t),  # 将同步任务，放到线程中去执行（由于GIL，一般是IO密集型任务）
        asyncio.sleep(1)
    )
    print("end", datetime.datetime.now())


asyncio.run(main())
