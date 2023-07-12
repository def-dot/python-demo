# inspect运行时检测
import inspect
import os


class T:
    def __init__(self, age):
        self.age = age


def getmembers_t():
    # getmembers 输出运行时__dict__（包括值）
    t = T(30)
    print(f"dir {dir(t)}")
    print(f"getmembers {inspect.getmembers(t)}")
    print(f"getmembers_static {inspect.getmembers_static(t)}")


def getmodulename_t():
    path = os.getcwd()  # 当前文件目录
    print(path)
    r = inspect.getmodulename(path)
    print(r)


if __name__ == '__main__':
    # getmembers_t()
    getmodulename_t()
