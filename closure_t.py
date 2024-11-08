def a():
    x = 1
    m = {}
    def b():
        # x = x+2 # error，未定义的引用
        y = x+1  # 使用外部变量
        x = 2
        y = m.update({"a": 1})
        m = ywei
        print(x)
    b()
    print(x)

def aa():
    x = 1
    m = {}
    def bb():
        # x = x+2 # error，未定义的引用
        # x = 2  # 会屏蔽外部的值
        y = x+1  # 使用外部变量
        print(y)

    bb()


# def a(x):
#     def b(y):
#         return x+y
#     return b
a()
