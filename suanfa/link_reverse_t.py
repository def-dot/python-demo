# 链表逆序
# https://leetcode.cn/problems/reverse-linked-list/


class Link:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def print_link(node):
    while node:
        print(node.data)
        node = node.next


def reverse_link_recursion(node):
    # 递归法
    if not node.next:
        return node
    head = reverse_link_recursion(node.next)
    node.next.next = node
    node.next = None
    return head


def reverse_link_iterate(node):
    # 迭代法
    head = None
    curr = node
    while curr:
        next = curr.next
        curr.next = head
        head = curr
        curr = next
    return head


if __name__ == '__main__':
    link2 = Link(2)
    link1 = Link(1, link2)
    print_link(link1)
    # res = reverse_link_recursion(link1)
    res = reverse_link_iterate(link1)
    print_link(res)
