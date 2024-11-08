"""
单列：多次实例化，指向的是同一个对象
"""

_instance = None


def normal_t():
    # 普通单例方式，变量为None则初始化，否则直接返回
    class Singleton:
        def __init__(self, host, port=6379):
            self.host = host
            self.port = port

    def get_singleton():
        global _instance
        if not _instance:
            _instance = Singleton('192.168.3.20')
        return _instance

    o1 = get_singleton()
    o2 = get_singleton()
    print(f'o1 {o1.host} {o1.port}')
    print(f"o1 is o2 {o1 == o2}")


def new_t():
    # __new__ 生成实例，因此可以重写__new__实现单例
    class Singleton:
        def __new__(cls, *args, **kwargs):
            if not hasattr(cls, "_instance"):
                cls._instance = super().__new__(cls, *args, **kwargs)
            return cls._instance

    sing1 = Singleton()
    print(f'sing1 {sing1}')
    sing2 = Singleton()
    print(f'sing2 {sing2}')
    print(f"is Singleton {sing1 is sing2}")


def metaclass_t():
    # 和__new__逻辑差不多
    # 类实例化过程，1.调用元类的__call__，类要被调用，必须调用类的__call__方法，类的__call__方法是在元类中定义的（对象的__call__方法是在类中定义的）
    # 2.调用类的__new__，创建实例化对象
    # 3.调用类的__init__，给实例化对象赋值
    class MetaClassT(type):
        def __call__(cls, *args, **kwargs):
            if not hasattr(cls, "_instance"):
                cls._instance = super().__call__(*args, **kwargs)
            return cls._instance

    class Singleton(metaclass=MetaClassT):
        pass

    sing1 = Singleton()
    print(f'sing1 {sing1}')
    sing2 = Singleton()
    print(f'sing2 {sing2}')
    print(f"is Singleton {sing1 is sing2}")


if __name__ == "__main__":
    normal_t()
    # new_t()
    # metaclass_t()
