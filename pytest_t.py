# 被测函数
def add(a, b):
    return a + b

# 测试用例：只需以 test_ 开头
def test_add_positive():
    assert add(1, 2) == 3

def test_add_negative():
    assert add(-1, -1) == -2

def test_string_inclusion():
    assert "pytest" in "hello pytest"


import pytest

def divide(a, b):
    return a / b

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (5, 5, 10),
    (2, 10, 12),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert a + b == expected


@pytest.fixture
def db_connection():
    # Setup: 模拟连接数据库
    db = {"data": "success"}
    yield db  # yield 之前是准备工作
    # Teardown: 模拟关闭连接
    print("\n关闭数据库连接")

def test_query(db_connection):
    # db_connection 会接收到 yield 出来的值
    assert db_connection["data"] == "success"
    print("查询数据库成功")