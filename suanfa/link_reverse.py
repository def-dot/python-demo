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
