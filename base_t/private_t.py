# python 通过_开头定义私有变量，私有变量仅表示变量不应该被访问，实际上仍能访问，python没有实际的访问限制

class T:
    def __init__(self):
        self._r = 1


t = T()
print(t._r)
