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


if __name__ == '__main__':
    attr_t()

