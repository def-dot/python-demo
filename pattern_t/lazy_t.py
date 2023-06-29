def calc_t():
    # 多次计算
    class Circle:
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            print('calcing.................')
            r = 3.14 * self.radius * self.radius
            return r

    c = Circle(5)
    r = c.area()
    r = c.area()


def calc_when_init_t():
    # 初始化时赋值
    class Circle:
        def __init__(self, radius):
            self.radius = radius
            self.area = self.calc()

        def calc(self):
            print('calcing.................')
            r = 3.14 * self.radius * self.radius
            return r

    c = Circle(5)
    r = c.area
    r = c.area


def calc_when_used_t():
    # 使用时赋值，仅一次
    class Circle:
        def __init__(self, radius):
            self.radius = radius
            self.area = None

        def calc(self):
            if not self.area:
                print('calcing.................')
                self.area = 3.14 * self.radius * self.radius
            return self.area

    c = Circle(5)
    r = c.calc()
    r = c.calc()


def calc_decor_t():
    # 更高级的优化，装饰器函数重写，原理还是判断是否有赋过值
    def once(func):
        def wrapper(instance, *args, **kwargs):
            if not hasattr(instance, "area"):
                instance.area = func(instance, *args, **kwargs)
            # instance.area
            return instance.area
        return wrapper

    class Circle:
        def __init__(self, radius):
            self.radius = radius

        @once
        def calc(self):
            print('calcing.................')
            area = 3.14 * self.radius * self.radius
            return area

    c = Circle(5)
    r = c.calc()
    print(r)
    r = c.calc()
    print(r)


def calc_desc_t():
    # 描述符，第一次会走类描述符，__get__将进行计算，并将计算结果赋值给实例描述符，对于非数据描述符，实例描述符优先类描述符，下一次会直接走实例描述符，返回已经计算好的结果。
    class Calc:
        def __init__(self, func):
            self.func = func

        def __get__(self, instance, owner):
            r = self.func(instance)
            instance.area = r
            return r


    class Circle:
        def __init__(self, radius):
            self.radius = radius

        @Calc  # area = Calc(area)
        def area(self):
            print('calc..........')
            area = 3.14 * self.radius * self.radius
            return area

    c = Circle(5)
    print(c.area)
    print(c.area)


if __name__ == '__main__':
    # calc_t()
    # calc_when_init_t()
    # calc_when_used_t()
    # calc_decor_t()
    calc_desc_t()

