class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def force(self, head: ListNode) -> bool:
        def ReverseList(head: ListNode) -> ListNode:
            res = None
            while head is not None:
                temp = head.next
                head.next = res
                res = head
                head = temp
            return res

        count = 0
        p = head
        while p:
            count += 1
            p = p.next

        if count == 1:
            return True

        mid = count / 2
        p = head
        for i in range(int(mid)-1):
            p = p.next
        t = p.next if mid == int(mid) else p.next.next

        tail = ReverseList(t)
        p.next = None

        while head and tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        return True


if __name__ == "__main__":
    node = ListNode(1)
    head = node

    # node.next = ListNode(2)
    # node = node.next
    #
    # # node.next = ListNode(3)
    # # node = node.next
    #
    # node.next = ListNode(2)
    # node = node.next
    #
    # node.next = ListNode(1)
    # node = node.next

    r = Solution().force(head)
    print(r)
