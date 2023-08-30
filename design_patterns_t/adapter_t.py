# 适配器，不同的类统一接口

class Dog:
    def __init__(self, name):
        self.name = name

    def wang(self):
        print(f"wangwang...{self.name}")


class Cat:
    def miao(self):
        print("miaomiao...")


class Car:
    def noise(self):
        print("noising...")


class Adapter:
    def __init__(self, obj, **kwargs):
        self.obj = obj
        self.__dict__.update(kwargs)


dog = Dog('laifu')
o = Adapter(dog, voice=dog.wang)
o.voice()
