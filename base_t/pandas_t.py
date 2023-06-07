import pandas
import pandas as pd


def series_t():
    # 一维数组，转换后可以理解为字典
    arr = ["apple", "banana", "car"]
    # 数组加上索引，转换为{"0": "apple", "1": "banana", "2": "car"}
    d = pd.Series(arr)
    print(f"series {d}")
    # 获取index=1的值
    print(f"series index 1 {d[1]}")
    # 指定索引
    d = pd.Series(arr, index=["fruit1", "fruit2", "fruit3"])
    print(f"assign index {d}")
    # 获取对应索引值
    print(f"get assign index {d['fruit1']}")


def dataframe_t():
    # 二维数组，转换后可以理解为字典数组
    arr = [["zhangsan", 20], ["lisi", 30]]
    # 数组加索引，转换为[{"name": "zhangsan", "age": "20"}, {"name": "lisi", "age": "30"}]
    d = pd.DataFrame(arr, columns=["name", "age"])
    print(f"arr DataFrame {d}")
    # 字典转换
    dic = {"name": ["zhangsan", "lisi"], "age": [20, 30]}
    d = pd.DataFrame(dic)
    print(f"dict DataFrame {d}")
    # 字典数组转换
    arr = [{"name": "zhangsan", "age": "20"}, {"name": "lisi", "age": "30"}]
    d = pd.DataFrame(arr)
    print(f"dic arr DataFrame {d}")
    # 返回指定行 loc
    print(f"get DataFrame loc {d.loc[0]}")
    print('---')
    print(f"get DataFrame loc {d.loc[1]}")
    # 指定索引（行名，默认是index 0 1 2）
    arr = [{"name": "zhangsan", "age": "20"}, {"name": "lisi", "age": "30"}]
    d = pd.DataFrame(arr, index=["student1", "student2"])
    print(f"assigned index {d}")
    # 获取指定索引
    print(f"get assigned index {d.loc['student1']}")
    # 获取指定列
    print(f"get assigned column {d['name']}")


def csv_t():
    # 二维数组 csv 导入导出
    pass


def json_t():
    # json转换，读json，json数据转为二维数组（json嵌套处理）
    pass


def transform_t():
    # 数据清洗处理，如去掉0值、去掉重复数据等
    pass


if __name__ == "__main__":
    # series_t()
    dataframe_t()
