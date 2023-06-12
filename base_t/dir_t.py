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


if __name__ == "__main__":
    dir_t()
    dict_t()
