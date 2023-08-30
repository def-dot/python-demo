# 线程不安全，需要加锁
# 加锁有两种方式

import threading

number = 0

lock = threading.Lock()


def add_unsafe():
    global number
    for i in range(1000000):
        number += 1


def add_safe():
    global number
    for i in range(1000000):
        # lock.acquire()
        with lock:
            number += 1
        # lock.release()


thread_1 = threading.Thread(target=add_safe)
thread_2 = threading.Thread(target=add_safe)

# thread_1 = threading.Thread(target=add_unsafe)
# thread_2 = threading.Thread(target=add_unsafe)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print(number)
