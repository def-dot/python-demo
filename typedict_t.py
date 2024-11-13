"""TypedDict和Pydantic功能和使用上类似；区别:
Pydantic会在运行时检查数据类型，而TypedDict不会检查，使用mypy工具检查类型是否有错误
Pydantic支持继承嵌套；TypedDict不支持
Pydantic字段可以设置可选，默认值；TypedDict默认必选，不支持默认值
"""

from typing_extensions import TypedDict


class Person(TypedDict):
    name: str
    age: int


p = Person(name="defdot", age="thirty")
print(p)
