# 合并两个有序链表

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def Merge(self, pHead1: ListNode, pHead2: ListNode) -> ListNode:
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


node = ListNode(1)
head1 = node

node.next = ListNode(3)
node = node.next

node.next = ListNode(5)
node = node.next

node = ListNode(2)
head2 = node

node.next = ListNode(4)
node = node.next

r = Solution().Merge(head1, head2)
while r:
    print(r.val)
    r = r.next
