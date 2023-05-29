# python调用C

import ctypes
import time


def python_t(num):
    result = 0
    for i in range(1, num+1):
        result += i
    print("result is %s" % result)


def c_t(num):
    c_dll = ctypes.cdll.LoadLibrary("./c_dll.so")
    c_dll.my_add(num)


if __name__ == "__main__":
    num = int(input("请输出整数"))
    start_time = time.time()
    python_t(num)
    end_time = time.time()
    print("python cost time %s" % (end_time - start_time))
    #
    # start_time = time.time()
    # c_t(num)
    # end_time = time.time()
    #
    # print("c cost time %s" % (end_time - start_time))
