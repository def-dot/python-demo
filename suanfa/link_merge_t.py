# 链表合并
# https://leetcode.cn/problems/merge-two-sorted-lists/solution/he-bing-liang-ge-you-xu-lian-biao-by-leetcode-solu/


class Link:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def print_link(node):
    while node:
        print(node.data)
        node = node.next


def merge_link_recursion(node1, node2):
    # 递归法
    if not node1:
        return node2
    elif not node2:
        return node1
    elif node1.data < node2.data:
        node1.next = merge_link_recursion(node1.next, node2)
        return node1
    else:
        node2.next = merge_link_recursion(node1, node2.next)
        return node2


def merge_link_iterate(node1, node2):
    # 迭代法
    root = Link(-1)
    head = root
    while node1 and node2:
        if node1.data < node2.data:
            head.next = node1
            node1 = node1.next
        else:
            head.next = node2
            node2 = node2.next
        head = head.next

    head.next = node1 if node1 else node2
    return root.next


if __name__ == '__main__':
    link2 = Link(3)
    link1 = Link(1, link2)

    link22 = Link(4)
    link11 = Link(2, link22)

    print_link(link1)
    print_link(link11)
    # res = merge_link_recursion(link1, link11)
    res = merge_link_iterate(link1, link11)
    print_link(res)
