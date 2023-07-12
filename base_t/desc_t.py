# 描述符,定义了__get__ __set__ __del__任一个的类
# 描述符其实是把属性的值委托给一个描述符类方法__get__ __set__，可以做属性值校验，或者返回处理后的属性值
import random


class Desc:
    def __get__(self, instance, owner):
        print(f"__get__")
        print(f"self {self}")  # Desc object
        print(f"instance {instance} owner {owner}")  # instance T object, owner T class
        return self

    def __set__(self, instance, value):
        print(f"__set__")


def class_attr_t():
    # 描述符是类的属性，等价于 ClassAttrT.__dict__['a'].__get__(t, ClassAttrT)
    class ClassAttrT:
        a = Desc()
    t = ClassAttrT()
    print(t.a)


def obj_attr_t():
    # 描述符是实例的属性，ClassAttrT.__dict__['a'].__get__(t, ClassAttrT)，ClassAttrT.__dict__['a'] 不存在，因为a是实例的属性，不会调用__get__
    class ClassAttrT:
        def __init__(self):
            self.a = Desc()

    t = ClassAttrT()
    print(t.a)


def class_obj_attr_t():
    # 描述符同时是类和实例的属性，当描述符定义了__set__或__del__，表示该描述符是一个数据描述符，描述符优先实例属性；
    # 若描述符只定义了__get__，没有定义__set__，表示该描述符是一个非数据描述符，实例属性优先描述符属性；
    class ClassAttrT:
        a = Desc()
        def __init__(self):
            self.a = 1

    t = ClassAttrT()
    print(t.a)


def attr_get_t():
    # 描述符，返回处理后的值10
    class Desc:
        def __get__(self, instance, owner):
            return 10

    class T:
        a = Desc()
    print(f"T.a {T.a}")
    t = T()
    print(f"t.a {t.a}")


def attr_get_set_t():
    # 描述符，返回处理后的值10
    class Desc:
        def __init__(self, value=20):
            self.value = value
        def __get__(self, instance, owner):
            print('__get__')
            return 10

        def __set__(self, instance, value):
            print('__set__')
            if value < 0:
                raise ValueError("必须大于或等于0")
            self.value = value

    class T:
        a = Desc()

        def __init__(self):
            self.a = -1
    t = T()
    print(f"t.a {t.a}")
    t.a = 35
    print(f"T.a {T.a}")
    t.a = -1
    print(f"T.a {t.a}")


def attr_return_t():
    # 描述符，根据条件，返回特定值
    class Desc:
        def __init__(self, num):
            self.num = num

        def __get__(self, instance, owner):
            if self.num == 1:
                return "apple"
            elif self.num == 2:
                return "banana"
            else:
                return "other"

    class T:
        a = Desc(4)

    print(T.a)


def attr_order_t():
    # 属性取值方法：__getattribute__
    # 非描述符 实例属性 > 类属性
    # 数据描述符__get__优先实例属性(__dict__不会包括数据描述符属性)
    # 实例属性优先非数据描述符__get__(__dict__会包括实例属性)
    class Desc:
        def __init__(self):
            self.value = 3

        def __get__(self, instance, owner):
            print('__get__')
            # return self.value
            return self.value

        # def __set__(self, instance, value):
        #     print('__set__')
        #     self.value = value + 1

    class T:
        # a = 2
        a = Desc()  # 描述符

        def __init__(self):
            self.a = 1

        def __getattribute__(self, item):
            print('__getattribute__')
            return super().__getattribute__(item)

    # print(T.__dict__)
    t = T()
    print(f't.__dict__ {t.__dict__}')  # __dict__也会调用__getattribute__，估计是在这里面赋值给__dict__
    print(t.a)
    print(T.a)


def func_t():
    # 函数中包括__get__方法，所以所有的函数都是非数据描述符
    def foo():
        pass
    # ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
    # '__get__', '__getattribute__', '__globals__', '__gt__', '__ha
    # sh__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subcl
    # asshook__']
    # print(dir(foo))

    class T:
        def f(self):
            pass

        def __init__(self):
            self.f = 2

    t = T()
    print(t.f)  # 实例优先 2


def validate_t():
    # 描述符用来做属性校验
    class Validate:
        def __init__(self):
            self.val = None

        def __get__(self, instance, owner):
            return self.val

        def __set__(self, instance, value):
            if self.valid(value):
                self.val = value
            else:
                raise ValueError

        def valid(self, value):
            pass

    class Num(Validate):
        def __init__(self, min, max):
            super().__init__()
            self.min = min
            self.max = max

        def valid(self, value):
            if isinstance(value, int) and self.min <= value <= self.max:
                return True
            else:
                return False

    class Str(Validate):
        def __init__(self, min_len, max_len):
            super().__init__()
            self.min_len = min_len
            self.max_len = max_len

        def valid(self, value):
            if isinstance(value, str) and self.min_len <= len(value) <= self.max_len:
                return True
            else:
                return False

    class T:
        a = Num(min=1, max=100)
        b = Str(min_len=3, max_len=20)

        def __init__(self, a, b):
            self.a = a
            self.b = b

    t = T(20, 'Bccc')
    print(t.a)
    print(t.b)


def decor_t():
    # 描述符用来做装饰器
    class mystaticmethod:
        def __init__(self, func):
            self.func = func

        def __get__(self, instance, owner):
            def f():
                return "haha"
            print(f'__get__')
            return f

    class T:
        @mystaticmethod  # foo=staticmethod(foo)
        def foo():
            return 1

        def __str__(self):
            return "haha"

    r = T.foo
    print(r)
    print(r())


def set_name_t():
    class Desc:
        def __set_name__(self, owner, name):
            print(f"__set_name__ owner {owner} name {name}")

    class T:
        d = Desc()


class ClsT:
    def attr_t(self):
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


    def del_t(self):
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
    # class_attr_t()
    # obj_attr_t()
    # class_obj_attr_t()
    # desc_t()
    # attr_return_t()
    # attr_get_set_t()
    # attr_order_t()
    # func_t()
    # validate_t()
    # decor_t()
    set_name_t()
    # ClsT().attr_t()
    # ClsT().del_t()


