import threading
import time

d = {
    "a": 1
}


def del_key():
    global d
    del d["a"]
    print("deleted")


def get_key():
    time.sleep(1)
    global d
    res = d["a"]
    print(res)


if __name__ == "__main__":
    t1 = threading.Thread(target=del_key)
    t2 = threading.Thread(target=get_key)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

