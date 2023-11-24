import threading
import time


def func1():
    while True:
        print("func1")
        time.sleep(10)
        break


def func2():
    while True:
        print("func2")
        time.sleep(10)


thread_1 = threading.Thread(target=func1)
thread_2 = threading.Thread(target=func2)

thread_1.start()
thread_2.start()

# thread_1.join()
# thread_2.join()

while True:
    time.sleep(1)
