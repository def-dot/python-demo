import datetime

import numpy as np
import datetime


def base_t():
    r = datetime.datetime.now()
    print(r)
    # 对角矩阵
    d = np.eye(4)
    print(f"eys {d}")
    # 一维数组
    d = np.array([1, 2, 3])
    print(f"one array {d}")
    # 二维数组
    d = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"two array {d}")
    # 最小维度
    d = np.array([1, 2, 3], ndmin=2)
    print(f"min dimension {d}")
    # 数据类型转换（complex 复数是什么？）
    d = np.array([1, 2, 3], dtype=complex)
    print(f"data type {d}")
    # dtype定义列字段名称，字段类型
    dtype = np.dtype([("name", "S20"), ("age", "i4")])
    d = np.array([('zhangsan', 20), ('lisi', 30)], dtype=dtype)
    print(f"data type {d}")
    # arange 循环range中数据，存放到一维数组
    d = np.arange(24)
    print(f"arange {d}")
    print(f"ndmin {d.ndim}")
    # reshape？ 2 4 3 说明是三维，2*4*3=24 元素个数
    d = d.reshape(2, 4, 3)
    print(f"reshape {d}")
    print(f"ndmin {d.ndim}")
    # shape 行数 列数
    d = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"shape {d.shape}")
    d = np.array([[1, 2, 3], [4, 5, 6]])
    d.shape = (3, 2)  # 改成三行两列
    print(f"change shape {d}")
    # itemsize 元素占用字节大小
    d = np.array([1, 2, 3], dtype=np.int8)
    print(f"itemsize {d.itemsize}")
    d = np.array([1, 2, 3], dtype=np.float64)
    print(f"itemsize {d.itemsize}")
    # flags 作用？
    d = np.array([1, 2, 3])
    print(f"flags {d.flags}")


def create_arr():
    # empty 指定shape的空数组(未初始化，值随机)
    d = np.empty((3, 2), dtype=int)
    print(f"empty {d}")
    # zeros 指定shape的数组，用0填充，默认类型为浮点数
    d = np.zeros((3, 2), dtype=int)
    print(f"zeros {d}")
    # ones 指定shape的数组，用1填充，默认类型为浮点数
    d = np.ones((3, 2), dtype=int)
    print(f"ones {d}")
    # ones_like 和传入的数组维度相同，元素用1填充；同理zeros_like
    d = np.array([1, 2, 3])
    d = np.ones_like(d)
    print(f"ones_like {d}")


if __name__ == "__main__":
    base_t()
    # create_arr()
