import threading
import time


def test1():
    while True:
        print("1")
        time.sleep(3)
        raise Exception("no")


def test2():
    while True:
        print("2")
        time.sleep(1)


t1 = threading.Thread(target=test1)
t1.start()
t2 = threading.Thread(target=test2)
t2.start()
t1.join()
t2.join()