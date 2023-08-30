# 实例状态共享，多个实例共享一个变量


def force_t():
    class Task:
        state = 'new'

        def __setattr__(self, key, value):
            super().__setattr__(key, value)
            if key == 'state':
                Task.state = value

        def __getattribute__(self, item):
            r = super().__getattribute__(item)
            if item == 'state':
                r = Task.state
            return r

    t1 = Task()
    t2 = Task()
    t1.state = 'running'
    t2.state = 'new'

    print(f"t1.state {t1.state}")
    print(f"t2.state {t2.state}")
    print(f"Task.state {Task.state}")


def pattern_t():
    # 实例的属性指向同一个引用
    class Task:
        _shared_state = {}

        def __init__(self):
            self.__dict__ = self._shared_state

    t1 = Task()
    t2 = Task()
    t1.state = 'running'
    t2.state = 'new'

    print(f"t1.state {t1.state}")
    print(f"t2.state {t2.state}")


if __name__ == "__main__":
    # force_t()
    pattern_t()
