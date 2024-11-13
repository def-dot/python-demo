import asyncio
from langchain_core.callbacks.manager import (
    adispatch_custom_event,
)
from langchain_core.runnables import RunnableLambda
from langchain_core.runnables.config import RunnableConfig


@RunnableLambda
async def foo(x: str) -> str:
    await adispatch_custom_event("event1", {"x": x})
    await adispatch_custom_event("event2", 5)
    return x



async def main():
    async for event in foo.astream_events("hello world", version="v2"):
        print(event)


asyncio.run(main())