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


def find_inherit_from_base():
    # 查询继承了base的所有类
    res = Base.registries
    return res


if __name__ == '__main__':
    r = find_inherit_from_base()
    print(r)

