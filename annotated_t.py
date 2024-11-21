from typing import Annotated


def zhushi():
    """
    仅仅作类型注释、说明
    """
    NotZeroInt = Annotated[int, "can not be 0"]

    def divide(num: NotZeroInt):
        print(10 / num)



def guiyue():
    """
    和归约函数一起用（给定数据列表，计算得到一个值），如sum、max 、 min等
    """
    import operator
    mylist = Annotated[list[int], operator.add]
    