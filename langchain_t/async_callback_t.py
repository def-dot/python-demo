import asyncio
from typing import Any, Dict, List, Optional
from uuid import UUID

from langchain_core.callbacks import AsyncCallbackHandler
from langchain_core.callbacks.manager import (
    adispatch_custom_event,
)
from langchain_core.runnables import RunnableLambda
from langchain_core.runnables.config import RunnableConfig


class AsyncCustomCallbackHandler(AsyncCallbackHandler):
    async def on_custom_event(
        self,
        name: str,
        data: Any,
        *,
        run_id: UUID,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> None:
        print(
            f"Received event {name} with data: {data}, with tags: {tags}, with metadata: {metadata} and run_id: {run_id}"
        )


@RunnableLambda
async def bar(x: str, config: RunnableConfig) -> str:
    """An example that shows how to manually propagate config.

    You must do this if you're running python<=3.10.
    """
    await adispatch_custom_event("event1", {"x": x}, config=config)
    await adispatch_custom_event("event2", 5, config=config)
    return x


async def main():
    async_handler = AsyncCustomCallbackHandler()
    await bar.ainvoke(1, {"callbacks": [async_handler], "tags": ["foo", "bar"]})


asyncio.run(main())
