# 两个链表的第一个公共节点


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def double_point(self, head1: ListNode, head2: ListNode) -> ListNode:
        p1 = head1
        p2 = head2
        while p1 != p2:
            p1 = head2 if not p1 else p1.next
            p2 = head1 if not p2 else p2.next
        return p1


if __name__ == "__main__":
    node = ListNode(1)
    head = node

    node.next = ListNode(5)
    node = node.next

    node.next = ListNode(3)
    node = node.next

    head2 = node

    r = Solution().double_point(head, head2)
    r = r.val if r else ''
    print(r)
