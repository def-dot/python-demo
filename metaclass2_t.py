"""
metaclass：元类，创建类的类
"""

class MyMeta(type):
    _instance = None

    def __new__(cls, cls_name, cls_base, cls_dict):
        print(f"-----------cls {cls}, cls_name {cls_name}, cls_base {cls_base}, cls_dict {cls_dict}")
        obj = super().__new__(cls, "fuck", cls_base, cls_dict)
        print(f"-------obj {obj}")
        return obj
    
    def __init__(cls, cls_name, cls_bases, cls_dict):
        cls.flag = "Y"  # cls = __new__创建的类
        print(f"--------cls {cls}")

    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class MyClass(metaclass=MyMeta):
    pass


a = MyClass()
b = MyClass()
print(a is b)
print(type(b).__name__)

