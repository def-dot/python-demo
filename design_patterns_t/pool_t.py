import queue


class ObjectPool:
    def __init__(self, q):
        self.q = q
        self.item = None

    def __enter__(self):
        if not self.item:
            self.item = self.q.get()
        return self.item

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.item:
            self.q.put(self.item)
            self.item = None


if __name__ == '__main__':
    q = queue.Queue()
    q.put("hello world")
    with ObjectPool(q) as obj:
        print(obj)
