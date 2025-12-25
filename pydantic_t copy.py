from pydantic import BaseModel


class Person(BaseModel):
    name: str
    age: int


class Article(BaseModel):
    title: str
    person: Person  # 支持嵌套


def struct_t():
    # 数据模型
    p = Person(name="a", age=10)
    print(p.name)


def valid_t():
    # 数据校验
    # p = Person(name="a", age="b")  # 错误
    p = Person(name="a", age="10")  # 正确，会自动进行类型转换
    print(p.age)


valid_t()
