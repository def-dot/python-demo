# 二叉树 前序 中序 后序遍历，最大深度，最小深度，叶子节点
# https://leetcode.cn/problems/binary-tree-inorder-traversal/solution/er-cha-shu-de-zhong-xu-bian-li-by-leetcode-solutio/
# https://blog.csdn.net/bone_ace/article/details/46718683


class BTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def preOrder(self):
        if self.data:
            print(self.data)
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()

    def inOrder(self):
        if self.left:
            self.left.inOrder()
        if self.data:
            print(self.data)
        if self.right:
            self.right.inOrder()

    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        if self.data:
            print(self.data)

    def levelOrder(self):
        queue = []
        queue.append(self)
        while queue:
            item = queue.pop(0)
            if item:
                print(item.data)
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)

    def depth(self):
        res = 0
        if not self:
            return res

        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0
        return max(left_depth, right_depth) + 1

    def leaves(self):
        if not self.left and not self.right:
            print(self.data)
        if self.left:
            self.left.leaves()
        if self.right:
            self.right.leaves()


def find_pre_order(node):
    if node.data is not None:
        print(node.data)
    if node.left:
        find_pre_order(node.left)
    if node.right:
        find_pre_order(node.right)


def find_leaves(node):
    if not node.left and not node.right:
        print(node.data)
    else:
        if node.left:
            find_leaves(node.left)
        if node.right:
            find_leaves(node.right)


def find_max_depth(node):
    if not node:
        return 0
    return 1 + max(find_max_depth(node.left), find_max_depth(node.right))


def find_min_depth(node):
    if not node:
        return 0
    if node.left and not node.right:
        return 1 + find_min_depth(node.left)
    if node.right and not node.left:
        return 1 + find_min_depth(node.right)
    return 1 + min(find_min_depth(node.left), find_min_depth(node.right))


if __name__ == '__main__':
    node_7 = BTree(7)
    node_8 = BTree(8)
    node_3 = BTree(3, node_7, node_8)
    node_9 = BTree(9)
    node_4 = BTree(4, node_9)
    node_1 = BTree(1, node_3, node_4)
    node_5 = BTree(5)
    node_6 = BTree(6)
    node_2 = BTree(2, node_5, node_6)
    node_0 = BTree(0, node_1, node_2)
    find_pre_order(node_0)

    # node_1.preOrder()
    # node_1.inOrder()
    # node_1.postOrder()
    # node_1.levelOrder()
    # res = node_0.depth()
    # print(res)
    # node_0.leaves()

    # print(find_min_depth(node_0))
