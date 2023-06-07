# python调用C

import ctypes

from common import cost


@cost
def python_t(num):
    result = 0
    for i in range(1, num+1):
        result += i
    print("result is %s" % result)


@cost
def c_t(num):
    c_dll = ctypes.cdll.LoadLibrary("./c_dll.so")
    c_dll.my_add(num)


if __name__ == "__main__":
    num = int(input("请输出整数"))
    # python_t(num)
    c_t(num)
