class Singleton:
    instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls.instances:
            instance = super().__new__(cls)
            cls.instances[cls] = instance
        return cls.instances[cls]


class T1()

s = Singleton()
s2 = Singleton()