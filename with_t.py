class CustomContextManager:
    def __init__(self) -> None:
        print("__init")
        self.name = "tetst"

    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        # if exc_type is not None:
        #     print(f"An exception of type {exc_type} occurred with value {exc_value}")
        #     return True
    def say(self):
        print(self.name)

# 使用自定义的上下文管理器
with CustomContextManager() as c:
    print(c)
    c.say()
    # 触发一个异常
    # raise ValueError("An error occurred")
