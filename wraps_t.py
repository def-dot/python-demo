# from functools import wraps


# def my_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         """我是包装层的描述"""
#         print("执行前...")
#         return func(*args, **kwargs)
#     return wrapper

# @my_decorator
# def say_hello(name):
#     """我是原函数的描述"""
#     print("Hello!", name)


from functools import wraps

# 第一层：负责接收装饰器自己的参数 (level)
def logger(level):
    # 第二层：这才是真正的装饰器，接收被装饰的函数 (func)
    def decorator(func):
        # 第三层：负责处理被装饰函数的参数 (*args, **kwargs)
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{level}] 正在调用 {func.__name__}...")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 使用时，先调用 logger("DEBUG")，它返回真正的 decorator
@logger(level="DEBUG")
def add(a, b):
    return a + b

print(add(1, 2))