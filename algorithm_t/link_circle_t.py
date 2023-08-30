# 判断链表是否有环


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def force(self, head: ListNode) -> bool:
        # 时间复杂度O(N) 空间复杂度O(N)
        existed = []
        while head:
            if head in existed:
                return True
            existed.append(head)
            head = head.next
        return False

    def double_point(self, head: ListNode) -> bool:
        # 快慢指针，快指针每次2步，慢指针每次1步
        # 时间复杂度O(N) 空间复杂度O(1)
        fast = head
        slow = head
        while fast and slow:
            fast = fast.next
            if slow.next:
                slow = slow.next.next
            else:
                return False
            if fast == slow:
                return True
        return False


if __name__ == "__main__":
    node = ListNode(1)
    head = node

    node.next = ListNode(5)
    node = node.next

    node.next = head

    r = Solution().double_point(head)
    print(r)



