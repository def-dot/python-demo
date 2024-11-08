import datetime
import threading
from concurrent.futures import ThreadPoolExecutor
from common import cost
import dis
import time
# 变量：值 引用
# 值类型（不可变），分配地址后（直接赋值），值不能被改变，值相同的变量指向同一地址。每个地址有引用计数统计，没有引用时，地址回收。
# 值类型：int string bool class
# 引用类型（可变），分配地址后（直接赋值），值可以更改，变量指向单独的地址空间。
# 引用类型：list dict set class
# 变量名表示指针，将一个变量赋给另一个变量时，这两个变量指向同一地址。
# 函数参数传递时，传递的都是引用


def value_t():
    # int
    a = 1000
    b = 1000
    print(f"int {id(a)} {id(b)} {a is b}")  # 不可变类型，对象内存地址相同
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


def str_t():
    # 拼接是一样的，指向同样的地址空间
    a = "hello_world"
    print(f"a {id(a)}")
    b = "hello_world"
    print(f"b {id(b)}")
    c = "hello" + "_" + "world"
    print(f"c {id(c)}")


def dict_t():
    class DictT(dict):
        def get(self, *args, **kwargs):
            return 3
        def __getattr__(self, item):
            return 2

    v = DictT()
    v["a"] = 1
    print(v.get('a'))
    print(v['a'])


def thread_t():
    t = ThreadPoolExecutor()  # 线程共用资源空间地址
    t.submit(refer_t)


class DictT:
    def max_value_t(self):
        d = {
            "a": 1,
            "b": 2,
            "c": 1
        }
        r = min(d, key=lambda x: d[x])
        print(r)

    def test(self):
        self.dict_t()  # cost 0.04296517372131348
        self.brace_t()  # cost 0.015957355499267578  {}比dict()快三倍，通过dis查看，dict需要函数调用
        self.dis_dict_brace()
        self.order_t()
        self.safe_t()  # 线程安全验证

    def safe_t(self):
        d = {
            "a": 1
        }

        def del_key():
            del d["a"]
            print("deleted")

        def get_key():
            time.sleep(1)
            res = d["a"]
            print(res)

        t1 = threading.Thread(target=del_key)
        t2 = threading.Thread(target=get_key)
        t1.start()
        t2.start()
        t1.join()
        t2.join()

    def dis_dict_brace(self):
        """
        dict-------------
100           0 LOAD_GLOBAL              0 (dict)
              2 CALL_FUNCTION            0
              4 POP_TOP
              6 LOAD_CONST               0 (None)
              8 RETURN_VALUE
        {}-------------
104           0 BUILD_MAP                0
              2 POP_TOP
              4 LOAD_CONST               0 (None)
        :return:
        """
        print("dict-------------")
        dis.dis(self.dict_t)
        print("{}-------------")
        dis.dis(self.brace_t)

    # @cost
    def dict_t(self):
        dict()

    # @cost
    def brace_t(self):
        {}

    def order_t(self):
        # 有序性（python3.6后字典已经是有序的了）
        r = {i: i for i in range(5)}
        print(r)
        r = {}
        r[5] = 1
        r[3] = 1
        r[6] = 1
        print(r)


class PrivateT:
    # python 通过_开头定义私有变量，私有变量仅表示变量不应该被访问，实际上仍能访问，python没有实际的访问限制
    def __init__(self):
        self._r = 1


def private_t():
    t = PrivateT()
    print(t._r)


class TimeT:
    def test(self):
        r = time.time()
        print(f"curr timestamp {r}")  # 1687319389.7015393 (秒) => 53年 =》 1970+53=》公元2023年
        t = time.strptime("2023-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
        r = time.mktime(t)
        print(f"2023-01-01 timestamp {r}")
        r = datetime.datetime.now()
        r = r.timestamp()
        print(f"datetime -> timestamp {r}")
        r = datetime.datetime.now()
        print(f"datetime minus {r}")


if __name__ == "__main__":
    # value_t()
    # DictT().test()
    # private_t()
    # TimeT().test()
    # refer_t()
    # thread_t()
    # time.sleep(5)
    # str_t()
    # dict_t()
    DictT().max_value_t()
