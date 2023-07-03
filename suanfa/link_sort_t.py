"""

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def dac(self, head: ListNode) -> ListNode:
        def Merge(pHead1: ListNode, pHead2: ListNode) -> ListNode:
            # write code here
            res = ListNode(-1)
            cur = res
            while pHead1 and pHead2:
                if pHead1.val > pHead2.val:
                    cur.next = pHead2
                    pHead2 = pHead2.next
                else:
                    cur.next = pHead1
                    pHead1 = pHead1.next
                cur = cur.next
            if pHead1:
                cur.next = pHead1
            if pHead2:
                cur.next = pHead2
            return res.next

        def divide(head: ListNode):
            if not head.next:
                return head
            # 分治
            fast_p = head
            slow_p = head
            while fast_p and fast_p.next and fast_p.next.next:
                fast_p = fast_p.next.next
                slow_p = slow_p.next

            t = slow_p.next
            slow_p.next = None
            left = head
            v1 = divide(left)
            right = t
            v2 = divide(right)
            res = Merge(v1, v2)
            return res

        res = divide(head)
        return res


if __name__ == "__main__":
    node = ListNode(1)
    head = node

    node.next = ListNode(3)
    node = node.next

    node.next = ListNode(2)
    node = node.next

    node.next = ListNode(4)
    node = node.next

    node.next = ListNode(5)
    node = node.next

    r = Solution().dac(head)
    while r:
        print(r.val)
        r = r.next
