# 链表指定区间翻转

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @param k int整型
# @return ListNode类
#
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        res = ListNode(-1)
        res.next = head
        t = res
        pre = None
        cur = None
        for i in range(0, m):
            pre = t
            cur = t.next
            t = t.next
        for i in range(m, n):
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp
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

r = Solution().reverseBetween(head, 2, 4)
while r:
    print(r.val)
    r = r.next
