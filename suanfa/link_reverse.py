# 链表指定区间翻转

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def ReverseList(self, head: ListNode) -> ListNode:
        # write code here
        res = None
        while head is not None:
            temp = head.next
            head.next = res
            res = head
            head = temp
        return res


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

r = Solution().ReverseList(head)
while r:
    print(r.val)
    r = r.next
