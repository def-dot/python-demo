# 链表最后K个节点


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def force(self, head: ListNode, k: int) -> ListNode:
        # 双指针
        count = 0
        first = head
        while first:
            count += 1
            first = first.next
        print(f"总长度 {count}")

        second = head
        while second:
            if count == k:
                return second
            second = second.next
            count -= 1

    def stack(self, head: ListNode, k: int) -> ListNode:
        # 压栈
        r = []
        while head:
            r.append(head.val)
            head = head.next

        r = r[-k:]
        p = ListNode(-1)
        node = p
        for i in r:
            node.next = ListNode(i)
            node = node.next
        return p.next


if __name__ == "__main__":
    node = ListNode(1)
    head = node

    node.next = ListNode(5)
    node = node.next

    node.next = ListNode(3)
    node = node.next

    r = Solution().stack(head, 2)
    while r:
        print(r.val)
        r = r.next
