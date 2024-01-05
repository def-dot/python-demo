class Tree:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def prev2(self, t):
        res = []
        def func(t):
            if not t:
                return
            res.append(t.val)
            func(t.left)
            func(t.right)
        func(t)
        return res

    def prev(self, t):
        if not t:
            return
        print(t.val)
        self.prev(t.left)
        self.prev(t.right)

    def middle(self, t):
        if not t:
            return
        self.middle(t.left)
        print(t.val)
        self.middle(t.right)

    def post(self, t):
        if not t:
            return
        self.post(t.left)
        self.post(t.right)
        print(t.val)


if __name__ == '__main__':
    t1 = Tree(1)
    t2 = Tree(2)
    t3 = Tree(3)
    t1.left = t2
    t1.right = t3
    # Solution().prev(t1)
    # Solution().middle(t1)
    # Solution().post(t1)
    Solution().prev2(t1)
