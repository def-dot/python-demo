import asyncio


async def nested(name, value):
    if name == "defdot":
        raise Exception("invalid name")
    return value


async def main():
    r = await asyncio.gather(
        nested("zhangsan", 1),
        nested("lisi", 2),
        nested("defdot", 3),
        return_exceptions=True  # 默认是False，程序会异常；为True时，异常会作为结果存到gather的结果中[1, 2, Exception('invalid name')]
    )
    print(r)


asyncio.run(main())
