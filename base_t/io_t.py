# GIL协作式
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


if __name__ == "__main__":
    t1 = threading.Thread(target=io_t1)
    t1.start()

    t2 = threading.Thread(target=io_t2)
    t2.start()

