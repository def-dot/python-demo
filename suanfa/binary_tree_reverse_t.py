# 二叉树翻转
# https://leetcode.cn/problems/invert-binary-tree/solution/fan-zhuan-er-cha-shu-by-leetcode-solution/


class BTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def reverse_tree(node):
    if not node:
        return node
    left = reverse_tree(node.left)
    right = reverse_tree(node.right)
    node.left = right
    node.right = left
    return node


def find_pre_order(node):
    if node.data is not None:
        print(node.data)
    if node.left:
        find_pre_order(node.left)
    if node.right:
        find_pre_order(node.right)


if __name__ == '__main__':
    node_1 = BTree(1)
    node_2 = BTree(2)
    node_0 = BTree(0, node_1, node_2)
    find_pre_order(node_0)
    reverse_tree(node_0)
    find_pre_order(node_0)

