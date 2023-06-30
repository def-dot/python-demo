# 判断链表是否有环
import time


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def check(self, head: ListNode) -> bool:
        existed = []
        while head:
            if head in existed:
                return True
            existed.append(head)
            head = head.next
        return False


if __name__ == "__main__":
    node = ListNode(1)
    head = node

    node.next = ListNode(5)
    node = node.next

    # node.next = head

    r = Solution().check(head)
    print(r)
