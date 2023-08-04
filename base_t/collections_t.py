from collections import namedtuple


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


if __name__ == '__main__':
    NamedTupleT().test()
