# 元类（类的基类，或者说类是元类的实例，使用元类创建类，约等于类和对象的关系）class方式创建类
class MyMetaClass(type):
    pass


def class_t():
    # class的方式创建类（实际也是基于type元类实例化）
    class Student(metaclass=MyMetaClass):
        country = "China"

        def __init__(self, name, age):
            self.name = name
            self.age = age

        def tell(self):
            print(f"hello, my name is {self.name}, come from {self.country}, I'm {self.age}")
    o = Student('zhangsan', 30)
    o.tell()


def type_t():
    # type的方式创建类
    class_name = 'Student'
    class_inherit = (object,)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell(self):
        print(f"hello, my name is {self.name}, come from {self.country}, I'm {self.age}")

    class_dict = {
        'country': 'China',
        '__init__': __init__,
        'tell': tell
    }
    # 一个类由三部分组成，类名、继承、方法和属性
    Student = MyMetaClass(class_name, class_inherit, class_dict)
    o = Student('lisi', 40)
    o.tell()


def new_t():
    # 测试__new__
    class Student(metaclass=MyMetaClass):
        country = "China"

        # __new__ create and return a new object，也就是类实例化，生成self，对象为空{}
        def __new__(cls, *args, **kwargs):
            print(f'__new__ {cls}')  # class Student 类本身
            print(f'__new__ args {args}')  # class Student 类本身
            print(f'__new__ kwargs {kwargs}')  # class Student 类本身
            obj = super().__new__(cls)
            print(f'__new__ {obj} {obj.__dict__}')   # 调用__new__ 创建类实例self，实例为空{}，不包含属性, __init__赋属性（方法呢？，方法、类属性都属于类，不属于实例？）
            return obj

        def __init__(self, name, age):
            print(f'__init__ {self}  {self.__dict__}')
            self.name = name
            self.age = age
            print(f'__init__ completed {self} {self.__dict__}')

        def tell(self):
            print(f"hello, my name is {self.name}, come from {self.country}, I'm {self.age}")

    o = Student('zhangsan', 30)
    print(f"o {o} {o.__dict__}")
    print(f"Student {Student} {Student.__dict__}")


def metaclass_t():
    # 元类的作用一：影响类的创建，元类的__new__能够校验类，new类。
    # 如：类本身和所有方法必须有文档说明__doc__，需要在生成类时进行校验，即元类中校验
    class MetaClassT(type):
        def __new__(cls, cls_name, cls_bases, cls_dict):
            print(f'MetaClassT __new__ {cls}')
            print(f'MetaClassT __new__ cls_name {cls_name}')
            print(f'MetaClassT __new__  cls_dict {cls_dict}')
            if '__doc__' not in cls_dict or not cls_dict.get('__doc__'):
                raise Exception('类本身必须有doc说明')
            for key in cls_dict:
                val = cls_dict.get(key)
                if not key.startswith('__') and callable(val) and not val.__doc__:
                    raise Exception('类方法必须有doc说明')

            obj = super().__new__(cls,  cls_name, cls_bases, cls_dict)
            print(f'MetaClassT cls {cls}')  # MetaClassT
            print(f'MetaClassT obj {obj}')  # Student
            return obj

        # def __init__(cls, cls_name, cls_bases, cls_dict):
        #     print(f'MetaClassT __init__ {cls}')  # Student
        #     print(f'MetaClassT __init__ cls_name {cls_name}')
        #     print(f'MetaClassT __init__  cls_bases {cls_bases}')
        #     print(f'MetaClassT __init__ cls_dict {cls_dict}')
        #     print(f'MetaClassT __init__ __dict__ {cls.__dict__}')
        #     if '__doc__' not in cls_dict or not cls_dict.get('__doc__'):
        #         raise Exception('类本身必须有doc说明')
        #     for key in cls_dict:
        #         val = cls.__dict__.get(key)
        #         if not key.startswith('__') and callable(val) and not val.__doc__:
        #             raise Exception('类方法必须有doc说明')
        #     super().__init__(cls_name, cls_bases, cls_dict)

    class Student(metaclass=MetaClassT):
        """
        this is class doc!
        """
        country = "China"

        def __init__(self, name, age):
            self.name = name
            self.age = age

        def tell(self):
            """
            this is tell doc!
            :return:
            """
            print(f"hello, my name is {self.name}, come from {self.country}, I'm {self.age}")

    o = Student('zhangsan', 30)
    o.tell()


def call_t():
    # 元类的作用二：影响类的实例化
    # 类实例化过程，1.调用元类的__call__，类要被调用，必须调用类的__call__方法，类的__call__方法是在元类中定义的（对象的__call__方法是在类中定义的）
    # 2.调用类的__new__，创建实例化对象
    # 3.调用类的__init__，给实例化对象赋值
    class MetaClassT(type):
        def __call__(cls, *args, **kwargs):
            # 调用__new__产生一个空对象obj
            print(f'__call__ cls {cls}')
            obj = cls.__new__(cls)
            print(f'__call__ {obj}')
            print(f'__call__ {obj.__dict__}')
            # 调用__init__初始化这个对象.
            cls.__init__(obj, *args, **kwargs)
            # 返回初始化的对象
            print(f'__call__ __init__ {obj.__dict__}')
            # 测试--控制实例属性隐藏
            print(cls.__name__)
            obj.__dict__ = {'_%s_%s' % (cls.__name__, key): val for key, val in obj.__dict__.items()}
            return obj

    class Student(metaclass=MetaClassT):
        """
        this is class doc!
        """
        country = "China"

        def __init__(self, name, age):
            self.name = name
            self.age = age

        def tell(self):
            """
            this is tell doc!
            :return:
            """
            print(f"hello, my name is {self.name}, come from {self.country}, I'm {self.age}")

    o = Student('zhangsan', 30)
    # print(o.name, o.age)
    print(o._Student_name, o._Student_age)
    print(o.__dict__)
    o.tell()


def singleton_t():
    pass


if __name__ == "__main__":
    # class_t()
    # type_t()
    # new_t()
    # metaclass_t()
    call_t()
