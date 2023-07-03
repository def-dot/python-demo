# 小端：从左到右，高端到低端存储（从高端开始存，或者说高字节存在内存的高位）

if __name__ == '__main__':
    s = "abc"
    print(f"{s} {id(s)}")
    for c in s:
        print(f"{c} {id(c)}")
