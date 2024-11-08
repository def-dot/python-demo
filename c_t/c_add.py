# python调用C

import ctypes
import threading
import time

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


def python_c_t():
    num = int(input("请输出整数"))
    python_t(num)
    c_t(num)


def p_sleep_t():
    print('p_sleep_t start')
    time.sleep(2)
    print('p_sleep_t end')


def multi_thread_t():
    c_dll = ctypes.cdll.LoadLibrary("./c_dll.so")
    c_dll.c_sleep_t(10)
    print('python go oning')
    time.sleep(1)
    thr = threading.Thread(target=p_sleep_t)
    thr.start()
    thr.join()


if __name__ == "__main__":
    # python_c_t()
    multi_thread_t()
