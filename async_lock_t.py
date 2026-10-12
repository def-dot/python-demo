import asyncio

value = 0

async def increment():
    global value
    await asyncio.sleep(0.01)
    value += 1

async def main():
    tasks = [asyncio.create_task(increment()) for i in range(10000)]
    await asyncio.gather(*tasks)
    print(f'Final value without lock: {value}')

if __name__ == "__main__":
    asyncio.run(main())