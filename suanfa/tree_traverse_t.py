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

    def back_traverse_t(self, root) -> list[list[int]]:
        res = []
        if not root:
            return res
        q = [[root]]
        index = 0
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

            if index % 2 != 0:
                curr_level.reverse()
            res.append(curr_level)
            index += 1
        return res

    def deep_t(self, root) -> int:
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

if __name__ == '__main__':
    """
         1
    2          3
4       5   6      7

1 
        2
    4      3
       5  6  7
pre: 1 2 4 5 3 6 7  == 1(l: r:2) 2(l:1 r:4) 
mid: 4 2 5 1 6 3 7  == 4(l: r:2) 2(l:4 r:5) 5(l:2 r:1) 1(l:5 r:6) 6(l:1 r:3) 3(l:6 r:7) 7(l:3 r:)
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

    t1.right = t2
    t2.left = t4
    t2.right = t3
    t4.right = t5
    t3.left = t6
    t3.right = t7

    # t1.left = t2
    # t1.right = t3
    #
    # t2.left = t4
    # t2.right = t5
    #
    # t3.left = t6
    # t3.right = t7

    r = Solution().pre_traverse_t(t1)
    print(r)
    # Solution().middle_traverse_t(t1)
    # Solution().post_traverse_t(t1)
    # r = Solution().level_traverse_t(t1)
    # r = Solution().back_traverse_t(t1)
    # r = Solution().deep_t(t1)
    # while r:
    #     print(r.val)
    #     r = r.right
