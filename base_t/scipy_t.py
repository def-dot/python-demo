import numpy as np
from scipy import constants
from scipy.sparse import csr_matrix
from scipy import io
from scipy import interpolate


def constants_t():
    # 常量（公制 二进制 体积 压强 温度等）
    # 1英亩对应多少平方米
    print(f"acre {constants.acre}")
    # pi
    print(f"pi {constants.pi}")
    # 黄金比例
    print(f"golden {constants.golden}")
    # 所有常量
    print(f"constants {constants}")


def optimize_t():
    # 优化
    pass


def arr_t():
    # 稀疏矩阵
    d = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])
    # 获取稀疏元素
    o = csr_matrix(d)
    print(f"csr_matrix {o} ")
    d = o.data
    print(f"csr_matrix data {d} ")
    d = o.count_nonzero()
    print(f"csr_matrix non zero count {d} ")
    # 删除矩阵中0元素
    o.eliminate_zeros()
    print(f"eliminate_zeros {o}")
    # 删除矩阵中重复项
    o.sum_duplicates()
    print(f"sum_duplicates {o}")


def graph_t():
    # 图结构，图可以用邻接矩阵表示，scipy可以支持图的最短路径、深度优先遍历、广度优先遍历等
    pass


def matlab_t():
    # matlab数据导入导出
    # d = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    # io.savemat("test.mat", {"vec": d})
    d = io.loadmat("test.mat")
    print(f"loadmat {d}")


def spatial_t():
    # 空间数据处理
    pass


def interpolate_t():
    # 插值，在两点之间根据算法平滑插入缺失值（不是很懂 插值算法？）
    xs = np.arange(10)
    ys = xs * 2 + 1
    print(xs)
    print(ys)
    interp_func = interpolate.interp1d(xs, ys)
    print(interp_func)
    d = interp_func(np.arange(2.1, 3, 0.1))
    print(d)


def stats_t():
    # 显著性校验（统计分析？）
    pass


if __name__ == "__main__":
    # constants_t()
    # arr_t()
    # matlab_t()
    interpolate_t()

