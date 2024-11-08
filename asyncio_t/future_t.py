import asyncio


async def delay(future, seconds, text):
    await asyncio.sleep(seconds)
    future.set_result(text)


async def main():
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    asyncio.create_task(delay(future, 1, "hello world"))
    print(await future)


asyncio.run(main())
