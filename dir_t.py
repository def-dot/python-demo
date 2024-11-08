class Person:
    country = 'China'

    def __init__(self, name):
        self.name = name

    def say(self):
        return f"hello ,my name is {self.name}"


class Student(Person):
    # def __init__(self, name, grade):
    #     super().__init__(name)
    #     self.grade = grade

    # def say(self):
    #     return f"hello ,my name is {self.name}, at {self.grade}"

    def study(self):
        return "I'm studing"


def dir_t():
    # 显示对象所有方法和属性（包含从父类继承来的）
    #  ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '
    # __reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'country', 'say', 'study']
    print(f"dir Student {dir(Student)}")
    s = Student("zhangsan")
    # 实例和类 dir结果一样
    print(f"dir s {dir(s)}")


def dict_t():
    # 只显示对象本身定义的方法和属性（不显示父类）
    # dict {'__module__': '__main__', 'study': <function Student.study at 0x0000020FB8D52A60>, '__doc__': None}
    print(f"dict Student {Student.__dict__}")
    s = Student("zhangsan")
    # 实例的__dict__只显示属性（实例其实只有属性，方法属于类，s.say()等价于Student.say(s)）
    print(f"dict s {s.__dict__}")


def dir_t2():
    class T:
        def __init__(self):
            self.name = 1

        def func_i(self):
            return 1

        @classmethod
        def func_c(cls):
            return 1

    print(dir(T))
    dir_t = ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
             '__getattribute__',
             '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__',
             '__new__',
             '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
             '__weakref__', 'test']
    print(f"__class__ {T.__class__}")  # 类的父类是type（元类）
    print(f"__class__ {T().__class__}")  # 实例的父类是class（类）
    print(f"__doc__ {T.__doc__}")
    print(f"__dict__ {T.__dict__}")
    print(f"__getattribute__ {T.__getattribute__}")  # __getattribute__(self, *args)
    print(f"__delattr__ {T.__delattr__}")  # __delattr__(self, *args)
    print(f"__setattr__ {T.__setattr__}")  # __setattr__(self, *args)
    print(f"__dir__ {T.__dir__}")  # __dir__(self, *args)
    print(f"__eq__ __ge__ __le__ __lt__ __gt__ __ne__ {T.__eq__}")  # __eq__(self, *args)
    print(f"func_i {T.func_i()}")  # func_i()
    print(f"func_c {T.func_c()}")  # func_c()
    # d = {'__module__': '__main__', '__init__': <function T.__init__ at 0x000001F946482940>, 'test': <function T.test at 0x000001F946482A60>, '__dict__': <attribute '__dict__' of 'T' objects>, '__weakref__': <attribute '__weakref__' of 'T' objects>, '__doc__': None}


if __name__ == "__main__":
    dir_t()
    dict_t()
    dir_t2()
