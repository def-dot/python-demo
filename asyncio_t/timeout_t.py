import asyncio


async def nested():
    await asyncio.sleep(5)
    return 1


async def main():
    try:
        async with asyncio.timeout(3):
            r = await nested()
            print(r)
    except asyncio.TimeoutError as e:
        print("timeout")


asyncio.run(main())
