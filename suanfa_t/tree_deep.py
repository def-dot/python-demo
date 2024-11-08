# 树 层序 前序 中序 后序 遍历
class Tree:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def deep(self, t):
        if not t:
            return 0
        return max(self.deep(t.left), self.deep(t.right)) + 1


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
    r = Solution().deep(t1)
    print(r)
