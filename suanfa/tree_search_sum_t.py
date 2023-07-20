import copy


class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def force_t(self, root, target):
        res = None
        def pp(root, path=[]):
            if not root:
                return
            path.append(root.val)

            if not root.left and not root.right:  # 叶子节点
                print(sum(path))
                if sum(path) == target:
                    print(path)
                    res = path

            if root.left:
                pp(root.left, copy.deepcopy(path))

            if root.right:
                pp(root.right, copy.deepcopy(path))

        pp(root)

        print(res)



if __name__ == '__main__':
    """
             1
        2               3
    4       5       6      7
8      9 10   11  12  13 14  15
sum 8 = 1->2->5
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
    r = Solution().force_t(t1, 8)
    print(r)
