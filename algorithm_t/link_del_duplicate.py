class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def force(self, head: ListNode) -> ListNode:
        p = head
        while p and p.next:
            q = p.next
            while q and p.val == q.val:
                q = q.next
            p.next = q
            p = p.next
        return head


if __name__ == "__main__":
    node = ListNode(1)
    head = node

    node.next = ListNode(1)
    node = node.next

    node.next = ListNode(2)
    node = node.next

    node.next = ListNode(2)
    node = node.next

    node.next = ListNode(2)
    node = node.next

    node.next = ListNode(4)
    node = node.next

    r = Solution().force(head)
    while r:
        print(r.val)
        r = r.next
