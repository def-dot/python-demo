import asyncio
from contextvars import ContextVar

current_order = None
current_order_var = ContextVar('current_order_var')


async def handle_order(name, dish):
    print(f"Processing order for {name}: {dish}")
    global current_order
    current_order = dish
    await asyncio.sleep(2)  # Simulate time taken to prepare the dish
    print(f"Order for {name} is ready: {current_order}")


async def handle_order_with_context(name, dish):
    print(f"Processing order for {name}: {dish}")
    current_order_var.set(dish)
    await asyncio.sleep(2)  # Simulate time taken to prepare the dish
    print(f"Order for {name} is ready: {current_order_var.get()}")


async def main():
    # await asyncio.gather(
    #     handle_order("张三", "清蒸鱼"),
    #     handle_order("李四", "红烧肉")
    # )
    await asyncio.gather(
        handle_order_with_context("张三", "清蒸鱼"),
        handle_order_with_context("李四", "红烧肉")
    )


if __name__ == "__main__":
    asyncio.run(main())
