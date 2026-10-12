import atexit

def goodbye(name, message="再见！"):
    print(f"{name}, {message} 程序正在关闭...")

# 注册函数
def test1():
    atexit.register(goodbye, "用户", message="感谢使用")
    print("test1运行中...")


def test2():
    print("test2运行中...")

test1()
test2()
