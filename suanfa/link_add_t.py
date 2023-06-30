# 两个链表，每个节点的值在0-9，计算两个链表相加的值，返回新的链表


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def force(self, head1: ListNode, head2: ListNode) -> ListNode:
        # 链表长度最长100，转换成int可能超过存储长度限制
        str1 = ""
        str2 = ""
        while head1:
            str1 += str(head1.val)
            head1 = head1.next
        while head2:
            str2 += str(head2.val)
            head2 = head2.next
        r = int(str1) + int(str2)
        root = ListNode(-1)
        head = root
        for i in str(r):
            node = ListNode(i)
            head.next = node
            head = head.next
        return root.next


if __name__ == "__main__":
    node = ListNode(1)
    head = node

    node.next = ListNode(5)
    node = node.next

    node.next = ListNode(3)
    node = node.next

    node = ListNode(1)
    head2 = node

    node.next = ListNode(9)
    node = node.next

    r = Solution().force(head, head2)
    while r:
        print(r.val)
        r = r.next

