def outer_function():
    def inner_function():
        return "Hello, World!"
    return inner_function  # 返回函数本身，而不是调用它

r = outer_function()
print(r)