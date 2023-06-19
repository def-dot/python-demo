# 合并多个有序链表
# 分治算法，分解成2个链表的合并

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def force_merge(self, links: list[ListNode]) -> ListNode:
        arr = []
        for i in links:
            while i:
                arr.append(i.val)
                i = i.next

        print(f"arr {arr}")
        arr.sort()

        head = ListNode(-1)
        res = head
        for i in arr:
            head.next = ListNode(i)
            head = head.next
        return res.next

    def Merge_two(self, pHead1: ListNode, pHead2: ListNode) -> ListNode:
        # write code here
        res = ListNode(-1)
        cur = res
        while pHead1 and pHead2:
            if pHead1.val > pHead2.val:
                cur.next = pHead2
                pHead2 = pHead2.next
            else:
                cur.next = pHead1
                pHead1 = pHead1.next
            cur = cur.next
        if pHead1:
            cur.next = pHead1
        if pHead2:
            cur.next = pHead2
        return res.next

    def dac_merge(self, links: list[ListNode]) -> ListNode:
        if not links:
            return None
        res = links.pop()
        while links:
            l = links.pop()
            res = self.Merge_two(res, l)
        return res


if __name__ == "__main__":
    node = ListNode(1)
    head1 = node

    node.next = ListNode(5)
    node = node.next

    node = ListNode(2)
    head2 = node

    node.next = ListNode(4)
    node = node.next

    node = ListNode(3)
    head3 = node

    links = [head1, head2, head3]

    # r = Solution().force_merge(links)
    r = Solution().dac_merge(links)
    while r:
        print(r.val)
        r = r.next
