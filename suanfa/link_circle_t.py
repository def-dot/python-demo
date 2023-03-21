# 环形链表判断
# https://leetcode.cn/problems/linked-list-cycle/


class Link:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def print_link(node):
    while node:
        print(node.data)
        node = node.next


def circle(node):
    # hash
    ht = {}
    while node:
        if node in ht:
            return True
        ht[node] = True
        node = node.next
    return False


if __name__ == '__main__':
    link2 = Link(2)
    link1 = Link(1, link2)
    link2.next = link1
    res = circle(link1)
    print(res)
