from dataclasses import dataclass, field, asdict

def test1():
    # 基本使用
    @dataclass
    class User:
        id: int
        name: str
        email: str

    user1 = User(1, "Alice", "alice@example.com")
    user2 = User(1, "Alice", "alice@example.com")

    print(user1)
    print(user1 == user2)


def test2():
    class User:
        def __init__(self, id: int, name: str, email: str):
            self.id = id
            self.name = name
            self.email = email

    user1 = User(1, "Alice", "alice@example.com")
    user2 = User(1, "Alice", "alice@example.com")
    print(user1)
    print(user1 == user2)  # 输出: False


def test3():
    # frozen 不可变
    @dataclass(frozen=True)
    class User:
        id: int
        name: str
        email: str

    user = User(1, "Alice", "alice@example.com")
    user.name = "Bob"  # 尝试修改属性将引发错误


def test4():
    # field使用
    @dataclass
    class User:
        id: int
        name: str
        email: str
        members: list[str] = field(default_factory=list)

    user = User(1, "Alice", "alice@example.com")
    user.name = "Bob"  # 尝试修改属性将引发错误


def test5():
    # 序列化
    @dataclass
    class User:
        id: int
        name: str
        email: str

    user1 = User(1, "Alice", "alice@example.com")
    print(asdict(user1))

if __name__ == "__main__":
    # test1()
    # test2()
    # test3()
    test5()