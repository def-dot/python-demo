# 两个链表，每个节点的值在0-9，计算两个链表相加的值，返回新的链表
# 反序各个节点相加，注意进位，结果反序输出


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

    def _reverse(self, head: ListNode) -> ListNode:
        # 反转
        res = None
        while head:
            t = head.next
            head.next = res
            res = head
            head = t
        return res

    def optimize(self, head1: ListNode, head2: ListNode) -> ListNode:
        # 1 5 3  +  1 9 ->  1 7 2
        res = ListNode(-1)
        p = res
        head1 = self._reverse(head1)
        head2 = self._reverse(head2)
        pre_carry = 0
        while head1 or head2:
            v1 = head1.val if head1 else 0
            v2 = head2.val if head2 else 0
            r = v1 + v2 + pre_carry
            if r >= 10:
                r = r % 10
                pre_carry = 1
            else:
                pre_carry = 0
            p.next = ListNode(r)
            p = p.next
            if head1:
                head1 = head1.next
            if head2:
                head2 = head2.next

        if pre_carry == 1:
            p.next = ListNode(pre_carry)
        res = res.next
        res = self._reverse(res)
        return res


if __name__ == "__main__":
    node = ListNode(9)
    head = node

    node.next = ListNode(3)
    node = node.next

    node.next = ListNode(7)
    node = node.next

    node = ListNode(6)
    head2 = node

    node.next = ListNode(3)
    node = node.next

    r = Solution().force(head, head2)
    while r:
        print(r.val)
        r = r.next
