# 链表是否有环
class Link:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def check(self, head):
        slow = head
        fast = head
        while slow and fast:
            if slow.next:
                slow = slow.next
            else:
                return False
            
            if head.next and head.next.next:
                head = head.next.next
            else:
                return False
            
            if slow == fast:
                return True


if __name__ == '__main__':
    l1 = Link(1)
    l2 = Link(2)
    l1.next = l2
    l3 = Link(3)
    l2.next = l3
    # l3.next = l1

    r = Solution().check(l1)
    print(r)
