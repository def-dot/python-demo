def force_t():
    # 查询继承了base的所有类
    registries = {}

    class Sub1:
        pass

    class Sub2:
        pass

    registries[Sub1.__name__] = Sub1
    registries[Sub2.__name__] = Sub2

    return registries


def optimize_t():
    # 查询继承了base的所有类
    class Base(type):
        registries = {}

        def __new__(cls, cls_name, cls_bases, cls_dict):
            obj = super().__new__(cls, cls_name, cls_bases, cls_dict)
            cls.registries[cls_name] = obj
            return obj

    class Sub1(metaclass=Base):
        pass

    class Sub2(metaclass=Base):
        pass
    res = Base.registries
    return res


def instance_force_t():
    # 实例注册
    registries = {}

    class Sub1:
        pass

    class Sub2:
        pass

    registries[Sub1.__name__] = Sub1()
    registries[Sub2.__name__] = Sub2()

    return registries


def instance_optimize_t():
    # 实例注册
    class Base:
        registries = {}
        # def __new__(cls, *args, **kwargs):
        #     obj = super().__new__(cls, *args, **kwargs)
        #     cls.registries[cls.__name__] = obj
        #     return obj

        def register(self):
            Base.registries[self.__class__.__name__] = self

    class Sub1(Base):
        pass

    class Sub2(Base):
        pass

    Sub1().register()
    Sub2().register()

    return Sub1.registries


if __name__ == '__main__':
    # r = force_t()
    # r = optimize_t()
    # r = instance_force_t()
    r = instance_optimize_t()
    print(r)
