import threading
import time

lock = threading.Lock()
a = 1


def my_read():
    # lock.acquire()
    for i in range(5):
        print(f"read {a}")
        time.sleep(1)
    # lock.release()


def my_write():
    lock.acquire()
    time.sleep(2)
    global a
    a = 2
    print(f"write {a}")
    lock.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=my_read)
    t2 = threading.Thread(target=my_write)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
