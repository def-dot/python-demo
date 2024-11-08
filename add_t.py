import sys
import time


def add(a, b):
    return a + b


if __name__ == "__main__":
    a = sys.argv[1]
    b = sys.argv[2]
    r = add(int(a), int(b))
    time.sleep(5)
    print(r)