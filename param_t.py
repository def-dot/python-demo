def param_t(a, b):
    # kv 方式赋值
    print(f"a {a} b {b}")


# def param_t2(a=1, b):
#     # 编译错误，默认值参数放后面
#     print(f"a {a} b {b}")


def param_t3(a, b=1):
    print(f"a {a} b {b}")


if __name__ == "__main__":
    # param_t(b=1, a=2)  # 支持kv方式赋值（可以无序），k为形参名称
    # param_t(b=1, c=2)  # 错误，异常的k
    # param_t(1, a=2)  # 错误，k多个值
    param_t(1, b=2)  # 对于args类型参数，顺序解析；对于kwargs类型参数，按形参名称解析
    # param_t3(1, b=3)
