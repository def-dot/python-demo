from typing import Protocol
from typing import Dict
from typing import Type


class Pet(Protocol):
    def speak(self):
        pass


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"喵喵喵......{self.name}")


class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"汪汪汪......{self.name}")


def pattern_t():
    def get_obj(name) -> Pet:
        animals: Dict[str, Type[Pet]] = {
            "dog": Dog,
            "cat": Cat
        }
        return animals[name]

    cls = get_obj("dog")
    o = cls("Wang")
    o.speak()


if __name__ == "__main__":
    pattern_t()


