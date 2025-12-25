def test1():
    """使用 match-case 语句进行模式匹配示例，相当于if-elif-else 结构。"""
    code = 400
    match code:
        case 200:
            print("OK")
        case 400:
            print("Bad Request")
        case _:
            print("unknown Status")


def test2():
    """参数解析，相当于函数"""
    command = ["move", 10, 20]

    match command:
        case ["move", x, y]:
            print(f"Moving to ({x}, {y})")
        case ["stop"]:
            print("Stopping")
            print(f"X={x}")
        case (0, y):
            print(f"Y={y}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            print("Not a point")


def test3():
    """grard守卫，先判断是不是int，如果是int，使用int()转换，并赋值给x，然后判断x的值"""
    data = -2
    match data:
        case int(x) if x > 0:
            print("正整数")
        case int(x):
            print("非正整数")
        case str(x):
            print("字符串")
        case _:
            print("其他类型")


def test4():
    """匹配对象"""
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    point = Point(1, 0)

    match point:
        case Point(x=0, y=0):
            print("原点")
        case Point(x=x, y=0):
            print(f"X轴上，x={x}")
        case Point(x=0, y=y):
            print(f"Y轴上，y={y}")
        case Point(x=x, y=y):
            print(f"点坐标为 ({x}, {y})")
        case _:
            print("其他情况")


if __name__ == "__main__":
    # test1()
    # test2()
    # test3()
    test4()