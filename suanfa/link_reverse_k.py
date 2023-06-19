# 链表中每K个元素翻转，不足K个不翻转

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # write code here
        res = ListNode(-1)
        res.next = head

        pre = res
        cur = head

        while True:
            t = cur
            for i in range(0, k):
                if not t:
                    return res.next
                t = t.next

            for i in range(1, k):
                target = cur.next
                cur.next = target.next
                target.next = pre.next
                pre.next = target

            if not cur.next:
                break

            pre = cur
            cur = cur.next

        return res.next

node = ListNode(1)
head = node

node.next = ListNode(2)
node = node.next

node.next = ListNode(3)
node = node.next

node.next = ListNode(4)
node = node.next

node.next = ListNode(5)
node = node.next

r = Solution().reverseKGroup(head, 3)
while r:
    print(r.val)
    r = r.next
