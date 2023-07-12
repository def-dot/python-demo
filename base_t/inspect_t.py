# inspect运行时检测
import inspect
import os


# this is a comment test
class T:
    """
    this is a doc test
    """
    def __init__(self, age):
        self.age = age


class TypeAndMembers:
    # 对象类型检查，对象自身属性获取
    def getmembers_t(self):
        # getmembers 输出运行时__dict__（包括值）
        t = T(30)
        print(f"dir {dir(t)}")
        print(f"getmembers {inspect.getmembers(t)}")
        print(f"getmembers_static {inspect.getmembers_static(t)}")

    def getmodulename_t(self):
        file_path = __file__
        print(f"file_path {file_path}")
        r = inspect.getmodulename(file_path)
        print(r)
        dir_path = os.path.dirname(__file__)
        print(f"dir_path {dir_path}")
        r = inspect.getmodulename(dir_path)  # base_t
        print(r)

    def type_t(self):
        # 实际调用isinstance
        r = inspect.ismodule(inspect)
        print(r)

        r = inspect.isclass(T)
        print(r)

        r = inspect.isfunction(T)
        print(r)


class RetriveSourceCode:
    # 获取源码相关
    def test(self):
        # 获取对象说明
        r = inspect.getdoc(T)
        print(r)

        # 获取object所在file D:\code\python-demo\base_t\inspect_t.py
        r = inspect.getfile(T)
        print(r)

        # 获取注释
        r = inspect.getcomments(T)
        print(r)

        # 获取module信息 <module 'inspect' from 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python39\\lib\\inspect.py'>
        r = inspect.getmodule(inspect)
        print(r)

        # 获取来源文件
        r = inspect.getsourcefile(T)  # D:\code\python-demo\base_t\inspect_t.py
        print(r)
        r = inspect.getsourcelines(T)  # (['class T:\n', '    """\n', '    this is a doc test\n', '    """\n', '    def __init__(self, age):\n', '        self.age = age\n'], 7)
        print(r)

        r = inspect.getsource(T)
        print(r)


class SignatureT:
    def foo(self):
        pass


if __name__ == '__main__':
    # TypeAndMembers().getmembers_t()
    # TypeAndMembers().getmodulename_t()
    # TypeAndMembers().type_t()
    RetriveSourceCode().test()
