import queue
class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def force_t(self, root: Tree) -> bool:
        # 层序
        if not root:
            return False
        q = [[root.left, root.right]]
        while q:
            curr_l = q.pop(0)
            if not curr_l:
                break

            if len(curr_l) % 2 != 0:
                return False

            for i in range(len(curr_l) // 2):
                l_v = curr_l[i].val if curr_l[i] else 0
                r_v = curr_l[-i-1].val if curr_l[-i-1] else 0
                if l_v != r_v:
                    return False

            next_l = []
            for i in curr_l:
                if i:
                    next_l.append(i.left)
                    next_l.append(i.right)
            q.append(next_l)
        return True

    def optimize(self, root: Tree) -> bool:
        # 层序
        if not root:
            return True

        q_l = queue.Queue()
        q_l.put(root.left)
        q_r = queue.Queue()
        q_r.put(root.right)

        while not q_l.empty() and not q_r.empty():
            l_node = q_l.get()
            r_node = q_r.get()

            if not l_node and not r_node:
                continue

            if not l_node or not r_node or l_node.val != r_node.val:
                return False

            q_l.put(l_node.left)
            q_l.put(l_node.right)

            q_r.put(r_node.right)
            q_r.put(r_node.left)

        return True

    def force_t2(self, root: Tree) -> bool:
        # 递归
        r1 = []
        r2 = []

        def left_right_traverse(root: Tree):
            if not root:
                return
            left_right_traverse(root.left)
            left_right_traverse(root.right)
            r1.append(str(root.val))

        def right_left_traverse(root: Tree):
            if not root:
                return
            right_left_traverse(root.right)
            right_left_traverse(root.left)
            r2.append(str(root.val))

        left_right_traverse(root)
        right_left_traverse(root)

        print(','.join(r1))
        print(','.join(r2))

        for i in range(len(r1)):
            if r1[i] != r2[i]:
                return False

        return True

    def optimize_t2(self, root: Tree) -> bool:
        # 递归
        def check(l_node, r_node):
            if not l_node and not r_node:
                return True

            if not l_node or not r_node or l_node.val != r_node.val:
                return False

            return check(l_node.left, r_node.right) and check(r_node.left, l_node.right)

        return check(root, root)


if __name__ == '__main__':
    """
             1
        2          2
    3       4   4     3

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
    t32 = Tree(4)
    t33 = Tree(4)
    t34 = Tree(5)

    t11.left = t21
    t11.right = t22

    t21.left = t31
    t21.right = t32

    t22.left = t33
    t22.right = t34

    # r = Solution().force_t(t11)
    # r = Solution().force_t2(t11)
    r = Solution().optimize_t2(t11)
    print(r)
