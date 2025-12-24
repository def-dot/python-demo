"""
惰性加载设计模式
1. from functools import cached_property
```
from functools import cached_property
import time

class DatabaseConnector:
    def __init__(self):
        print("初始化对象...")

    @cached_property
    def connection(self):
        print("正在建立耗时的数据库连接...")
        time.sleep(2)  # 模拟耗时操作
        return "Connected_to_DB"

# 测试
db = DatabaseConnector()
print("对象已创建，但连接尚未建立。")
print(f"第一次访问: {db.connection}")  # 触发计算
print(f"第二次访问: {db.connection}")  # 直接从缓存读取，不打印“建立连接”
```
2. @property
```
class BigDataModel:
    def __init__(self):
        self._data = None

    @property
    def data(self):
        if self._data is None:
            print("正在从硬盘加载大数据...")
            self._data = [i for i in range(1000000)]
        return self._data

model = BigDataModel()
# 此时 model.data 还是 None，内存占用低
```
3. 延迟导入
```
def process_image(path):
    # 只有调用此函数时，才会加载重量级的 PIL 库
    from PIL import Image
    img = Image.open(path)
    # ... 处理逻辑
```
"""


def calc_t():
    # 多次计算
    class Circle:
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            print('calcing.................')
            r = 3.14 * self.radius * self.radius
            return r

    c = Circle(5)
    r = c.area()
    r = c.area()


def calc_when_init_t():
    # 初始化时赋值
    class Circle:
        def __init__(self, radius):
            self.radius = radius
            self.area = self.calc()

        def calc(self):
            print('calcing.................')
            r = 3.14 * self.radius * self.radius
            return r

    c = Circle(5)
    r = c.area
    r = c.area


def calc_when_used_t():
    # 使用时赋值，仅一次
    class Circle:
        def __init__(self, radius):
            self.radius = radius
            self.area = None

        def calc(self):
            if not self.area:
                print('calcing.................')
                self.area = 3.14 * self.radius * self.radius
            return self.area

    c = Circle(5)
    r = c.calc()
    r = c.calc()


def calc_decor_t():
    # 更高级的优化，装饰器函数重写，原理还是判断是否有赋过值
    def once(func):
        def wrapper(instance, *args, **kwargs):
            if not hasattr(instance, "area"):
                instance.area = func(instance, *args, **kwargs)
            # instance.area
            return instance.area
        return wrapper

    class Circle:
        def __init__(self, radius):
            self.radius = radius

        @once
        def calc(self):
            print('calcing.................')
            area = 3.14 * self.radius * self.radius
            return area

    c = Circle(5)
    r = c.calc()
    print(r)
    r = c.calc()
    print(r)


def calc_desc_t():
    # 描述符，第一次会走类描述符，__get__将进行计算，并将计算结果赋值给实例描述符，对于非数据描述符，实例描述符优先类描述符，下一次会直接走实例描述符，返回已经计算好的结果。
    class Calc:
        def __init__(self, func):
            self.func = func

        def __get__(self, instance, owner):
            r = self.func(instance)
            instance.area = r
            return r


    class Circle:
        def __init__(self, radius):
            self.radius = radius

        @Calc  # area = Calc(area)
        def area(self):
            print('calc..........')
            area = 3.14 * self.radius * self.radius
            return area

    c = Circle(5)
    print(c.area)
    print(c.area)


if __name__ == '__main__':
    # calc_t()
    # calc_when_init_t()
    # calc_when_used_t()
    # calc_decor_t()
    calc_desc_t()

