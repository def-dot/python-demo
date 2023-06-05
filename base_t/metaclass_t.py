# class方式创建类
class Person(object):
    count = "China"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell(self):
        print("name: %s age: %s" % (self.name, self.age))


p = Person("test", 20)
p.tell()


# type方式创建类
count = 'China'


def __init__(self, name, age):
    self.name = name
    self.age = age


def tell(self):
    print("name: %s age: %s" % (self.name, self.age))


Employee = type("Employee", (object,), {'count': count, '__init__': __init__, 'tell': tell})
e = Employee("test2", 30)
e.tell()

