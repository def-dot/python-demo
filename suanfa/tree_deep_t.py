class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def force_t(self, root) -> int:
        if not root:
            return 0
        res = 0
        q = [[root]]
        while q:
            res += 1
            nodes = q.pop(0)
            next_level = []
            for i in nodes:
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            if next_level:
                q.append(next_level)

        return res

    def optimize_t(self, root) -> int:
        """
        终止条件： 当进入叶子节点后，再进入子节点，即为空，没有深度可言，返回0.
        返回值： 每一级按照上述公式，返回两边子树深度的最大值加上本级的深度，即加1.
        本级任务： 每一级的任务就是进入左右子树，求左右子树的深度。
        :param root:
        :return:
        """
        if not root:
            return 0
        return max(self.optimize_t(root.left), self.optimize_t(root.right)) + 1


if __name__ == '__main__':
    """
         1
    2          3
4       5   6      7
pre: 1 2 4 5 3 6 7
mid: 4 2 5 1 8 6 3 7
post: 4 5 2 6 7 3 1
level: 1 2 3 4 5 6 7
back: 1 3 2 4 5 6 7
    """
    t4 = Tree(4)
    t5 = Tree(5)
    t6 = Tree(6)
    t7 = Tree(7)
    t2 = Tree(2)
    t3 = Tree(3)
    t1 = Tree(1)

    t1.left = t2
    t1.right = t3

    t2.left = t4
    t2.right = t5

    t3.left = t6
    t3.right = t7

    # r = Solution().force_t(t1)
    r = Solution().optimize_t(t1)
    print(r)
