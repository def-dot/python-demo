# 删除链表的第K个节点


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def force(self, head: ListNode, n: int) -> ListNode:
        # 双指针
        count = 0
        first = head
        while first:
            count += 1
            first = first.next
        print(f"总长度 {count}")

        second = head
        while second:
            if count == n:
                return second.next
            elif count == n + 1:
                second.next = second.next.next
                return head
            else:
                second = second.next
                count -= 1


if __name__ == "__main__":
    node = ListNode(1)
    head = node

    node.next = ListNode(5)
    node = node.next

    # node.next = ListNode(3)
    # node = node.next

    r = Solution().force(head, 2)
    while r:
        print(r.val)
        r = r.next
