# 顺时针打印矩阵


def row_column_convert(arr):
    # 行列转换
    r = []
    while True:
        t = arr.pop(0)
        r += t
        new_arr = []
        if not arr:
            break
        for i in range(len(arr[0])):
            line = []
            for j in range(len(arr)):
                line.append(arr[j][len(arr[0]) - i - 1])
            new_arr.append(line)
    return r


if __name__ == "__main__":
    arr = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    r = row_column_convert(arr)
    print(r)

