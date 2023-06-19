import datetime
from concurrent.futures import ThreadPoolExecutor
# 值 引用
# 值类型（不可变），分配地址后（直接赋值），值不能被改变，值相同的变量指向同一地址。每个地址有引用计数统计，没有引用时，地址回收。
# 值类型：int string bool class
# 引用类型（可变），分配地址后（直接赋值），值可以更改，变量指向单独的地址空间。
# 引用类型：list dict set class
# 变量名表示指针，将一个变量赋给另一个变量时，这两个变量指向同一地址。
# 函数参数传递时，传递的都是引用


def value_t():
    # int
    a = 1
    b = 1
    print(f"int {id(a)} {id(b)}")  # 不可变类型，对象内存地址相同
    a = 2
    print(f"int change {id(a)}")  # 重新赋值，创建新的对象，变量指向新的对象
    # string
    d = "hello world"
    e = "hello world"
    f = "hello"
    print(f"string {id(d)} {id(e)} {id(f)}")
    # tuple
    a = (1, 2, )
    b = (1, 2,)
    print(f"tuple {id(a)} {id(b)}")

    def param_t(x):
        print(f"param xingcan {id(x)}")
        x = 3
        print(f"param xingcan {id(x)}")

    param_t(1)


def refer_t():
    # 除了基本的值类型，其他的都是引用，都会分配新的空间
    # list
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(f"array {id(a)} {id(b)}")  # a b 内存地址不同，和值类型不同
    b = a
    print(f"array {id(a)} {id(b)}")  # b=a a和b指向相同的内存地址
    a.append(4)
    print(f"array {id(a)} {id(b)}")  # b=a a和b指向相同的内存地址
    # dict
    a = {"a": 1}
    b = {"a": 1}
    print(f"dict {id(a)} {id(b)}")  # b=a a和b指向相同的内存地址
    # set
    a = {1, 2}
    b = {1, 2}
    print(f"set {id(a)} {id(b)}")  # b=a a和b指向相同的内存地址
    # class
    class A:
        def __init__(self, val):
            self.val = val
    a = A
    b = A
    print(f"class {id(a)} {id(b)}")
    a = A(1)
    b = A(1)
    print(f"obj {id(a)} {id(b)}")
    a = datetime.date(2023, 6, 16)
    b = datetime.date(2023, 6, 16)
    print(f"datetime {id(a)} {id(b)}")

    def param_t(x):
        print(f"param xingcan {id(x)}")

    a = [1, 2, 3]
    print(f"param shican {id(a)}")
    param_t(a)


def thread_t():
    t = ThreadPoolExecutor()  # 线程共用资源空间地址
    t.submit(refer_t)


if __name__ == "__main__":
    value_t()
    refer_t()
    # thread_t()
    # time.sleep(5)
