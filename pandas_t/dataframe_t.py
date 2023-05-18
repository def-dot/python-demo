import pandas

data = {
    "name": ["a", "b", "c"],
    "age": [1, 2, 3]
    # "age": [1, 2, 3, 4]  error, 数组len必须一致
}

res = pandas.DataFrame(data)
print(res)
