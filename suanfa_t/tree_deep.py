# 树 层序 前序 中序 后序 遍历
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
    
    def level(self, t):
        import queue
        q = queue.Queue()
        r = []
        if not t:
            return r
        q.put(t)
        while not q.empty():
            c = []
            n = q.qsize()
            for i in range(n):
                node = q.get()
                c.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            r.append(c)                
        return r
          
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
    t4 = Tree(4)
    t5 = Tree(5)
    t1.left = t2
    t1.right = t3
    t3.left = t4
    t4.right = t5
    # Solution().prev(t1)
    # Solution().middle(t1)
    # Solution().post(t1)
    # Solution().prev2(t1)
    r = Solution().level(t1)
    print(r)
