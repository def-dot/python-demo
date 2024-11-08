# import asyncio
#
#
# async def nested(seconds):
#     await asyncio.sleep(seconds)
#
#
# async def main():
#     # r = asyncio.current_task()
#     # print(r)
#     r = asyncio.iscoroutine(main)
#     print(r)
#
#     task1 = asyncio.create_task(nested(1), name="t1")
#     task2 = asyncio.create_task(nested(2), name="t2")
#     r = asyncio.all_tasks()
#     print(r)
#
#     await asyncio.gather(task1, task2)
#
#
# asyncio.run(main())

import asyncio

async def my_coroutine():
    await asyncio.sleep(1)

async def main():
    async def inner_coroutine():
        await asyncio.sleep(1)

    is_coro1 = asyncio.iscoroutine(my_coroutine)
    is_coro2 = asyncio.iscoroutine(main)
    is_coro3 = asyncio.iscoroutine(inner_coroutine)

    print("Is coroutine:", is_coro1)
    print("Is coroutine:", is_coro2)
    print("Is coroutine:", is_coro3)

asyncio.run(main())
