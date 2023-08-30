def nested_t():
    class Nest:
        def do(self):
            print("worker doing...")

    class Main:
        def run(self):
            n = Nest()
            n.do()

    o = Main()
    o.run()


def inject_init_t():
    # 通过构造函数
    class Nest:
        def do(self):
            print("worker doing...")

    class Main:
        def __init__(self, worker):
            self.worker = worker

        def run(self):
            self.worker.do()

    n = Nest()
    o = Main(n)
    o.run()


def inject_setter_t():
    # 通过setter设置
    class Nest:
        def do(self):
            print("worker doing...")

    class Main:
        def __init__(self):
            self.worker = None

        def set(self, worker):
            self.worker = worker

        def run(self):
            self.worker.do()

    o = Main()
    o.set(Nest())
    o.run()


if __name__ == '__main__':
    # nested_t()
    # inject_init_t()
    inject_setter_t()
