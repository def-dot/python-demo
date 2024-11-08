# GIL协作式
import subprocess
import sys
import threading
import time


def io_t1():
    with open("test.txt", "w") as f:
        print(f"t1 {threading.currentThread().ident} running, {time.time()}")
        for i in range(1000000):
            f.write("hello world")
    print(f"t1 {threading.currentThread().ident} completed, {time.time()}")


def io_t2():
    print(f"t2 {threading.currentThread().ident} running, {time.time()}")
    time.sleep(0.1)
    print(f"t2 {threading.currentThread().ident} completed, {time.time()}")


class StdT:
    def std_print_t(self):
        # 标准输出stdout 是行缓冲，当遇到换行符时，会立即输出，否则等缓冲区满了(512B)才输出
        print("1")
        print("2")

    def std_write_t(self):
        sys.stdout.write("1")
        sys.stdout.write("2")


    def std_err_t(self):
        # stderr会立马输出
        sys.stdout.write("1")
        sys.stderr.write("2")
        sys.stdout.write("3")

    def std_wrap_t(self):
        # \n会立马输出
        sys.stdout.write("1\n")
        sys.stderr.write("2")
        sys.stdout.write("3")

    def std_subprocess_t(self):
        # 输出1 2 3；当输出结果重定向到文件时，print会缓存，输出 2 1 3
        print(1)
        subprocess.run("echo 2", shell=True, check=True)
        print(3)


if __name__ == "__main__":
    # t1 = threading.Thread(target=io_t1)
    # t1.start()
    #
    # t2 = threading.Thread(target=io_t2)
    # t2.start()

    # StdT().std_print_t()
    # StdT().std_write_t()
    StdT().std_err_t()  # 不使用缓存的方法，1. python -u io_t.py 2. export PYTHONUNBUFFERED=1
    # StdT().std_wrap_t()
    # StdT().std_subprocess_t()
