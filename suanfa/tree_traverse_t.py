import queue
class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pre_traverse_t(self, root: Tree) -> list[int]:
        res = []
        if not root:
            return res

        def pre(tree, res):
            res.append(tree.val)
            if tree.left:
                pre(tree.left, res)
            if tree.right:
                pre(tree.right, res)

        pre(root, res)
        return res

    def middle_traverse_t(self, root):
        res = []
        if not root:
            return res

        def middle(tree, res):
            if tree.left:
                middle(tree.left, res)
            res.append(tree.val)
            if tree.right:
                middle(tree.right, res)

        middle(root, res)
        return res

    def post_traverse_t(self, root):
        res = []
        if not root:
            return res

        def post(tree, res):
            if tree.left:
                post(tree.left, res)
            if tree.right:
                post(tree.right, res)
            res.append(tree.val)

        post(root, res)
        return res

    def level_traverse_t(self, root) -> list[list[int]]:
        res = []
        if not root:
            return res
        q = [[root]]
        while q:
            nodes = q.pop(0)
            next_level = []
            curr_level = []
            for i in nodes:
                curr_level.append(i.val)
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            if next_level:
                q.append(next_level)

            res.append(curr_level)
        return res


if __name__ == '__main__':
    """
         1
    2          3
4       5   6      7
pre: 1 2 4 5 3 6 7
mid: 4 2 5 1 8 6 3 7
post: 4 5 2 6 7 3 1
level: 1 2 3 4 5 6 7
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

    # r = Solution().pre_traverse_t(t1)
    # print(r)
    # Solution().middle_traverse_t(t1)
    # Solution().post_traverse_t(t1)
    r = Solution().level_traverse_t(t1)
    print(r)
