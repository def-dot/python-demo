def attr_t():
    # 实例属性访问顺序：实例属性 > 类属性 > 父类属性 >  __getattr__
    class F:
        # a = 3
        pass

    class T(F):
        # a = 1

        def __init__(self):
            # self.a = 2
            pass

        def __getattr__(self, item):
            return 4

    t = T()
    print(t.a)


def del_t():
    # __del__的使用，在作用域结束后，会由解释器调用释放，也可以手动调用
    class T:
        def __init__(self, name):
            self.name = name

        def __del__(self):
            print(f"name {self.name} is deleted")

    def auto():
        t1 = T('张三')

    auto()
    print('over')


if __name__ == '__main__':
    # attr_t()
    del_t()


