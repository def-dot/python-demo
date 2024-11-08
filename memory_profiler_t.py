# 性能测试工具 memory_profiler
import threading
import queue
import time


class T:
    def __init__(self):
        self.q = queue.Queue()
        self.start()

    def produce(self):
        while True:
            for i in range(10):
                self.q.put(1)
            print(f'produce.... {self.q.qsize()}')
            time.sleep(1)

    def consume(self):
        while True:
            for i in range(5):
                self.q.get()
            print(f'consume.... ')
            time.sleep(1)

    def start(self):
        t1 = threading.Thread(target=self.produce)
        t1.start()
        t2 = threading.Thread(target=self.consume)
        t2.start()


if __name__ == '__main__':
    T()
    while True:
        time.sleep(60)
