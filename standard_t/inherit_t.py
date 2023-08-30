def self_t():
    # 子类实例化后，调用父类方法，self仍然指向的是子类实例化对象。
    class A:
        def display(self):
            print(self.__class__.__name__)

    class B(A):
        def display(self):
            super().display()
            print(self.__class__.__name__)

    o = B()
    o.display()  # 输出B B


def mro_t():
    # 方法解析顺序（MRO），使用的是C3算法
    # C3算法的核心是：1.递归，子类D的MRO=D+merge(L(B),L(C),B,C) 2.merge的原则是第一个元素不在其他merge元素的尾部（非第一个元素），则pop
    class A:
        def display(self):
            print('A')

    class B(A):
        def display(self):
            super().display()
            print('B')

    class C(A):
        def display(self):
            super().display()
            print('C')

    class D(B, C):
        def display(self):
            super().display()
            print('D')

    # C3解析过程
    # L(D) = D + merge(L(B), L(C), B, C) => L(D) = D + merge((B, A, OBJECT), (C, A, OBJECT), B, C)
    #                                    => L(D) = D + B + merge((A, OBJECT), (C, A, OBJECT), C)
    #                                    => L(D) = D + B + C + merge((A, OBJECT), (A, OBJECT))
    #                                    => L(D) = D + B + C + A + merge((OBJECT), (OBJECT))
    #                                    => L(D) = D + B + C + A + OBJECT
    # L(B) = B + merge(L(A), A) => L(B) = B + merge((A, OBJECT), A) => L(B) = B + A + OBJECT
    # L(C) = C + merge(L(A), A) => L(C) = C + merge((A, OBJECT), A) => L(C) = C + A + OBJECT
    # L(A) = A + merge(L(OBJECT), OBJECT)  => L(A) = A + OBJECT

    print(D.mro())
    o = D()
    o.display()


def mixin_t():
    # mixin 混入，实际上是继承，依赖MRO链，可以调用上层方法（某种情况下，类本身没有直接继承上层方法，所以本身无法调用）
    class A:
        def display(self):
            super().display()
            print('A')

    class B(A):
        def display(self):
            super().display()
            print('B')

    class C:
        def display(self):
            print('C')

    class D(B, C):
        def display(self):
            super().display()
            print('D')

    # C3解析过程
    # L(D) = D + merge(L(B), L(C), B, C) => L(D) = D + merge((B, A, OBJECT), (C, OBJECT), B, C)
    #                                    => L(D) = D + B + merge((A, OBJECT), (C, OBJECT), C)
    #                                    => L(D) = D + B + A + merge((OBJECT),  (C, OBJECT), C)
    #                                    => L(D) = D + B + A + C + merge((OBJECT), (OBJECT))
    #                                    => L(D) = D + B + A + C + OBJECT
    # L(B) = B + merge(L(A), A) => L(B) = B + merge((A, OBJECT), A) => L(B) = B + A + OBJECT
    # L(C) = C
    # L(A) = A + merge(L(OBJECT), OBJECT)  => L(A) = A + OBJECT
    print(D.mro())
    o = D()
    o.display()


if __name__ == "__main__":
    # self_t()
    # mro_t()
    mixin_t()
