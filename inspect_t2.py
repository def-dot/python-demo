import inspect
def example_func(a: int, b="hello", *args, **kwargs) -> str:
    return "result"
sig = inspect.signature(example_func)
print(sig.parameters) 
# 输出: (a: int, b='hello', *args, **kwargs) -> str


class A:
    """This is class A"""
    def __init__(self, x: int, y: str = "default"):
        self.x = x
        self.y = y

    def method_one(self):
        pass

    def method_two(self):
        pass


sig = inspect.signature(A)

print(sig.parameters) 
