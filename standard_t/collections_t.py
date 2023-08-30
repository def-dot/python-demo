import re
import time
from collections import namedtuple, OrderedDict, deque, defaultdict, Counter, ChainMap


class NamedTupleT:
    def test(self):
        TypeMapping = namedtuple("TypeMapping", ["name", "ip_k", "sbbm_k"], defaults=[1, 2, 3])
        t1 = TypeMapping(name="sxj", ip_k="ip", sbbm_k="sbbm")
        print(f"{t1} {t1.name} {t1.ip_k}")
        t2 = TypeMapping._make(['pc', 'ip', 'sbbm'])
        print(f"{t2} {t2.name} {t2.ip_k}")
        print(f"{t2._asdict()}")
        t2 = t2._replace(ip_k="IPDZ")
        print(f"{t2.ip_k}")
        print(f"{t2._fields}")
        t3 = TypeMapping()
        print(t3._asdict())
        print(t3._field_defaults)
        print(f"getattr(t3, 'name') {getattr(t3, 'name')}")

        class TestT(TypeMapping):
            def __str__(self):
                return f"TypeMapping name: {self.name} ip_k: {self.ip_k}"

        t4 = TestT()
        print(str(t4))


class OrderedDictT:
    def test(self):
        d = OrderedDict()
        d["a"] = 1
        d["b"] = 2
        d["c"] = 3
        print(f"{d}")
        d.move_to_end("a")
        print(f"move_to_end {d}")
        d.popitem(0)  # 1: last  0: first
        print(f"popitem {d}")


class DequeT:
    def tail(self):
        with open("test.txt", "rb") as f:
            r = deque(f)
            print(f"len {len(r)}")
            for i in r:
                print(i.decode('utf-8'))
            print('------------')
            time.sleep(1)


class DefaultDictT:
    def test(self):
        d = defaultdict(int)
        a = "hello world"
        for i in a:
            d[i] += 1  # 默认是int类型，值为0，简化代码，自动处理None值
            # if i not in d:
            #     d[i] = 0
            # d[i] += 1
        print(d)


class CounterT:
    def test(self):
        import jieba
        content = open("test.txt", "rb").read()
        words = jieba.cut(content)
        r = Counter(words)
        r = r.most_common(10)
        print(r)
        c = Counter(cat=4, dog=8)
        print(c['cat'])
        c = Counter({'cat': 4, 'dog': 8})
        print(c['cat'])


class ChainMapT:
    def test(self):
        a = {"a": 1, "b": 2}
        b = {"b": 3, "c": 4}
        # a.update(b)
        c = ChainMap(a, b)
        c['b'] = 5
        print(f"c {c} {c['b']} {c['c']}")
        print(f"a {a}")
        print(f"b {b}")


if __name__ == '__main__':
    # NamedTupleT().test()
    # OrderedDictT().test()
    # DequeT().tail()
    # DefaultDictT().test()
    # CounterT().test()
    ChainMapT().test()
