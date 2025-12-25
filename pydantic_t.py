from pydantic import BaseModel
from dataclasses import dataclass


class UserPY(BaseModel):
    id: int
    username: str
    email: str


@dataclass
class UserDC:
    id: int
    username: str
    email: str


def test1():
    # 类型校验
    user1 = UserDC(id="dd", username="Alice", email="")
    print(user1)

    user1 = UserPY(id="dd", username="Alice", email="")
    print(user1)


def test2():
    # 序列化
    user1 = UserPY(id=1, username="Alice", email="")
    # print(user1.model_dump())
    print(user1.model_dump_json())

if __name__ == "__main__":
    # test1()
    test2()
