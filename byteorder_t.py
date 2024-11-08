# 小端：从左到右，高端到低端存储（从高端开始存，或者说高字节存在内存的高位）
import struct


def little_big_endian():
    import sys
    print(f"byteorder {sys.byteorder}")

    s = "abc"
    print(f"{s} {id(s)}")
    for c in s:
        print(f"{c} {id(c)}")
    x = 'a'
    print(f"{x} {id(x)}")


def struct_t():
    values = (1, b'ab', 2.7)
    f = 'I 2s f'
    s = struct.Struct(f)
    packed_data = s.pack(*values)
    print(f"size {s.size}")
    print(f"packed_data {packed_data}")


if __name__ == '__main__':
    # little_big_endian()
    struct_t()
