import sys
import datetime
from decimal import Decimal


'''
占用空间解释
/* PyObject_VAR_HEAD defines the initial segment of all variable-size

container objects. These end with a declaration of an array with 1

element, but enough space is malloc'ed so that the array actually

has room for ob_size elements. Note that ob_size is an element count,

not necessarily a byte count.

*/

typedef uint32_t digit

struct _long object{
    PyObject_VAR_HEAD
    digit ob_digit[1];
};

define PyObject_VAR_HEAD PyVarObject ob_base;

typedef struct{
    PyObject ob_base;
    Py_ssize_tob_size;  /* Number of items in variable part */
} PyVarObject;

typedef struct _object{
    _PyObject_HEAD_EXTRA
    Py_ssize_t ob_refcnt;
    struct _typeobject *ob_type;
} PyObject;


# 64位系统，最小24位，增量4字节（ob_digit为0时不占空间）
struct PyLongObject{
    long ob_refcnt;// 8 bytes
    struct _typeobject *ob_type;// 8 bytes
    long ob_size;// 8 bytes
    unsigned int ob_digit[1];// 4 bytes * abs(ob_size)
};

# 32位，最小12位，增量2字节（ob_digit为0时不占空间）
struct PyLongObject{
    int ob_refcnt;// 4 bytes
    struct _typeobject *ob_type;// 4 bytes
    int ob_size;// 4 bytes
    unsigned short ob_digit[1];// 2 bytes * abs(ob_size)
};
'''


def size_t():
    # 占用空间大小
    r = 0
    print(f'type(r) {type(r)}')
    print(f"r.__sizeof__() {r.__sizeof__()}")
    print(f"sys.getsizeof(0) {sys.getsizeof(0)}")
    print(f"sys.getsizeof(1) {sys.getsizeof(1)}")
    print(f"sys.maxsize {sys.maxsize}")  # 9223372036854775807
    print(f"type of sys.maxsize {type(sys.maxsize)}")


def type_t():
    # 不可变：number str bool tuple datetime  可变：list dict set
    # number: int float complex
    a, b, c = 1, 1.5, 3+4j
    print(f"number type {type(a)}, {type(b)}, {type(c)}")
    # str
    d = "hello"
    print(f"str type {type(d)}")
    # tuple 不能更新
    e = ("A", "B", "C")
    print(f"tuple type {type(e)}")
    # list 有序
    f = [1, 2, 3]
    print(f"list type {type(f)}")
    f.append("A")
    print(f"list append {f}")
    g = {"a": 1, "b": 2}
    # dict 无序
    print(f"dict type {type(g)}")
    g.update({"c": 3})
    print(f"dict update {g}")
    # set 不会有重复 无序
    h = {"A", "B"}
    print(f"set type {type(h)}")
    h.add("C")
    h.add("C")
    print(f"set add {h}")
    # datetime
    i = datetime.datetime.now()
    print(f"datetime {i} type {type(i)}")


def type_convert_t():
    # 数据类型转换
    # datetime -> str
    i = datetime.datetime.now()
    print(f"{i} {type(i)}")
    i_str = str(i)
    print(f"to str {i_str} {type(i_str)}")
    i_str = i.strftime("%Y-%m-%d %H:%M:%S")
    print(f"to str {i_str} {type(i_str)}")
    # float ->int
    j = 1.5
    print(f"{j} {type(j)}")
    j_int = int(j)
    print(f"to int {j_int} {type(j_int)}")


def float_t():
    # float精度丢失问题；round不准确问题；format格式化输出也是不准确的（round和format逻辑一致，四舍五入位是5时不准确，但不清楚逻辑是什么）；
    a = 0.1
    b = 0.2
    print(f"flat a {a}")
    print(f"flat b {b}")
    print(f"float 计算 {a+b}")  # 0.30000000000000004
    # print(f"numpy float 计算 {core.float128(a) + core.float128(b)}")  # 0.30000000000000004
    a = 1.5
    b = 2.5
    print(f"round a {a} {round(a)}")  # 2
    print(f"round b {b} {round(b)}")  # 2
    a = 2.15
    b = 2.25
    c = 2.35
    print(f"round a {a} {round(a, 1)}")  # 2.1 ?
    print(f"round b {b} {round(b, 1)}")  # 2.2 ?
    print(f"round c {c} {round(c, 1)}")  # 2.4
    c = 1.4
    print(f"round c {c} {round(c)}")  # 1
    # format
    a = 1.15
    print("format {:.1f}".format(a))
    a = 1.16
    print("format {:.1f}".format(a))
    a = 3.14159
    print("format {:.3f}".format(a))
    a = 3.14159
    print(f"round a {a} {round(a, 3)}")  # 1


def decimal_t():
    a = 0.1
    b = 0.2
    print(f"flat a {a}")
    print(f"flat b {b}")
    print(f"float 计算 {a + b}")  # 0.30000000000000004
    a = Decimal(str(a))
    b = Decimal(str(b))
    c = a + b
    print(f"decimal 计算 {c} {type(c)}")  # 0.3


def ord_t():
    # 返回单个字符的unicode值
    r = ord('a')
    print(f"ord a {r}")  # 97
    r = ord('汉')  # error, string of length 3 found
    print(f"ord 汉 {r}")
    print(f"len 汉 {len('汉')}")
    r = ord('123')  # error, string of length 3 found
    print(f"ord 123 {r}")


if __name__ == "__main__":
    # size_t()
    # type_t()
    # type_convert_t()
    # float_t()
    # decimal_t()
    ord_t()
