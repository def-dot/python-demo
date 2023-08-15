class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def optimize(self, p1: Tree, p2: Tree) -> Tree:
        def merge_t(p1, p2):
            if not p1:
                return p2
            if not p2:
                return p1

            head = Tree(p1.val + p2.val)
            head.left = merge_t(p1.left, p2.left)
            head.right = merge_t(p1.right, p2.right)
            return head

        return merge_t(p1, p2)

    def pre_traverse(self, root):
        if not root:
            return
        print(root.val)
        self.pre_traverse(root.left)
        self.pre_traverse(root.right)


if __name__ == '__main__':
    """
             1
        2          2
    3       
    
            5
        1      3
          2       6

pre: 1 2 4 5 3 6 7  == 1(l: r:2) 2(l:1 r:4) 
mid: 4 2 5 1 6 3 7  == 4(l: r:2) 2(l:4 r:5) 5(l:2 r:1) 1(l:5 r:6) 6(l:1 r:3) 3(l:6 r:7) 7(l:3 r:)
post: 4 5 2 6 7 3 1
level: 1 2 3 4 5 6 7
back: 1 3 2 4 5 6 7
    """
    t11 = Tree(1)
    t21 = Tree(2)
    t22 = Tree(2)
    t31 = Tree(3)

    t11.left = t21
    t11.right = t22

    t21.left = t31


    p11 = Tree(5)
    p21 = Tree(1)
    p22 = Tree(3)
    p32 = Tree(2)
    p34 = Tree(6)

    p11.left = p21
    p11.right = p22
    p21.right = p32
    p22.right = p34

    # r = Solution().force_t(t11)
    # r = Solution().force_t2(t11)
    r = Solution().optimize(t11, p11)
    Solution().pre_traverse(r)
