# 描述符,定义了__get__ __set__ __del__任一个的类


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


if __name__ == '__main__':
    # class_attr_t()
    # obj_attr_t()
    class_obj_attr_t()
