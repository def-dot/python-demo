class Solution:
    def removeNthFromEnd(self , head , n ):
        # write code here
        if not head:
            return None
        # 定义快慢指针
        slow = head
        fast = head
        for i in range(n):
            fast = fast.next
        # 判断n是否大于head的长度
        if not fast:
            return head.next
        # 快慢指针同时行走
        while fast.next:
            fast = fast.next
            slow = slow.next
        # 删除结点
        slow.next = slow.next.next
        return head
