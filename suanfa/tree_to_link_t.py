import queue
class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    head = None
    p = None

    def convert_to_double_link(self, root: Tree) -> Tree:
        if not root:
            return None

        self.convert_to_double_link(root.left)
        if not self.head:
            self.head = root
            self.p = root
        else:
            root.left = self.p
            self.p.right = root
            self.p = root

        self.convert_to_double_link(root.right)

        return self.head


if __name__ == '__main__':
    """
         1
    2          2
4       5   6      7


         1
    2          2
3       4   4     3
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

    t1.left = t2
    t1.right = t3

    t2.left = t4
    t2.right = t5

    t3.left = t6
    t3.right = t7

    r = Solution().convert_to_double_link(t1)
    while r:
        print(r.val)
        r = r.right
