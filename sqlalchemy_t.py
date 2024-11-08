# sqlalchemy 异步

import asyncio
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

ASYNC_SQLALCHEMY_URI = 'mysql+aiomysql://root:root@127.0.0.1/test'
async_engine = create_async_engine(ASYNC_SQLALCHEMY_URI, pool_recycle=1500)
async_session = sessionmaker(async_engine, class_=AsyncSession)


async def get():
    # query
    async with async_session() as session:
        result = await session.execute(text('select * from simple'))
        data = result.fetchall()
        print(data)


async def add():
    # add
    async with async_session() as session:
        async with session.begin():
            await session.execute(text('insert into simple values("wangwu", 50),("lisi", 20)'))


async def update():
    # update
    pass


async def delete():
    # delete
    pass


async def run():
    await get()
    # await add()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
