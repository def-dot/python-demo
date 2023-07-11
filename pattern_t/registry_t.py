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


class Sub3(metaclass=Base):
    pass


def force_t():
    # 查询继承了base的所有类
    print(Sub1.__bases__)


def optimize_t():
    # 查询继承了base的所有类
    res = Base.registries
    return res


if __name__ == '__main__':
    # r = force_t()
    r = optimize_t()
    print(r)
