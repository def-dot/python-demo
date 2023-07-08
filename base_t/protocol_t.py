import abc
from typing import Union
from typing import Protocol


def abc_t():
    # 抽象基类
    class Animal(abc.ABC):
        @abc.abstractmethod  # 简单将函数对象的__isabstractmethod__属性置为True
        def run(self):
            pass

    class Dog(Animal):
        def run(self):
            print("dog run")

    def pet_run(pet: Animal):
        pet.run()

    o = Dog()
    pet_run(o)


def protocol_t():
    # duck-typing 协议，必须实现Protocol中的所有方法（参数、返回值不影响），静态属性值一致，才是该类型
    # go就是很典型的鸭子类型语言
    class Animal(Protocol):
        name = "Animal"

        def run(self, v=1):
            pass

    class Dog:
        name = "Animal"

        def run(self, a, b):
            print("dog run")
            return a + b

        def eat(self):
            print("dog eat")

    def pet_run(pet: Animal):
        pet.run()

    o = Dog()
    pet_run(o)


def union_t():
    # union指定多个类型
    class Dog:
        def run(self):
            print("dog run")

    class Cat:
        def run(self):
            print("cat run")

    def pet_run(pet: Union[Dog, Cat]):
        pet.run()

    o = Dog()
    pet_run(o)


if __name__ == "__main__":
    # union_t()
    abc_t()
