import pandas

data = ["a", "b", "c"]  # 一维数组
res = pandas.Series(data)
print(res)

data = ["a", "b", "c"]  # 一维数组
res = pandas.Series(data, index=[1, 2, 3])
print(res)


data = {"x": "a", "y": "b", "z": "c"}  # 字典, key会被当作索引
res = pandas.Series(data)
print(res)


data = {"x": "a", "y": "b", "z": "c"}  # 只取一部分列
res = pandas.Series(data, index=["x", "y"])  # 定义不存在的索引，返回NaN
print(res)


data = {"x": "a", "y": "b", "z": "c"}  # 只取一部分列
res = pandas.Series(data, index=["x", "y"], name="s_name")  # 设置series名称
print(res)
