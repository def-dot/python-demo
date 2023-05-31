import pandas

data = {
    "name": ["a", "b", "c"],
    "age": [1, 2, 3]
    # "age": [1, 2, 3, 4]  error, 数组len必须一致
}
res = pandas.DataFrame(data)
print(res)

data = [["a", 1], ["b", 2], ["c", 3]]
res = pandas.DataFrame(data)  # 没有定义列名，默认用序号 0 1
print(res)

data = [["a", 1], ["b", 2], ["c", 3]]
res = pandas.DataFrame(data, columns=["name", "age"])
print(res)

data = {"name": ["a", "b", "c"], "age": [1, 2, 3]}
res = pandas.DataFrame(data)
print(res)

data = [{"name": "a", "age": 1}, {"name": "b", "age": 2}]
res = pandas.DataFrame(data)
print(res)
