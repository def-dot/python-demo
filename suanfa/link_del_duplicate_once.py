class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def force(self, head: ListNode) -> ListNode:
        p = head
        root = ListNode(-1)
        root_p = root
        while p:
            flag = True
            q = p.next
            while q and p.val == q.val:
                flag = False
                q = q.next
            if flag:
                root_p.next = p
                root_p = root_p.next
            else:
                if not q:
                    root_p.next = None
            p = q
        return root.next


if __name__ == "__main__":
    node = ListNode(1)
    head = node

    node.next = ListNode(1)
    node = node.next

    node.next = ListNode(2)
    node = node.next

    # node.next = ListNode(4)
    # node = node.next

    r = Solution().force(head)
    while r:
        print(r.val)
        r = r.next
