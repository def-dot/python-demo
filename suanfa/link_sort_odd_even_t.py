class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self , head: ListNode) -> ListNode:
         #如果链表为空，不用重排
        if head == None:
            return head
        #even开头指向第二个节点，可能为空
        even = head.next
        #odd开头指向第一个节点
        odd = head
        #指向even开头
        evenhead = even
         # 1 3 2 4
        while even and even.next:
            #odd连接even的后一个，即奇数位
            odd.next = even.next
            #odd进入后一个奇数位
            odd = odd.next
            #even连接后一个奇数的后一位，即偶数位
            even.next = odd.next
            #even进入后一个偶数位
            even = even.next
        #even整体接在odd后面
        odd.next = evenhead
        return head


class Solution:
    def force(self, head: ListNode) -> ListNode:
        even = ListNode(-1)
        even_p = even
        odd = ListNode(-1)
        odd_p = odd
        count = 0
        while head:
            count += 1
            if count % 2 == 0:
                even_p.next = head
                even_p = even_p.next
            else:
                odd_p.next = head
                odd_p = odd_p.next
            head = head.next

        if count % 2 != 0:
            even_p.next = None
            odd_p.next = even.next
        else:
            odd_p.next = even.next
        odd = odd.next
        return odd

    def optimize(self, head: ListNode) -> ListNode:
        odd = head
        even = head.next
        even_p = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_p
        return head


if __name__ == "__main__":
    node = ListNode(1)
    head = node

    node.next = ListNode(3)
    node = node.next

    node.next = ListNode(2)
    node = node.next

    node.next = ListNode(4)
    node = node.next

    r = Solution().optimize(head)
    while r:
        print(r.val)
        r = r.next
