# 链表反序
# https://www.nowcoder.com/practice/75e878df47f24fdc9dc3e400ec6058ca?tpId=295&tqId=23286&ru=/exam/oj&qru=/ta/format-top101/question-ranking&sourceUrl=%2Fexam%2Foj
class Link:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


def reversed_link(head):
    res = None
    while head:
        temp = head.next
        head.next = res
        res = head
        head = temp
    return res

if __name__ == '__main__':
    l1 = Link(1)
    l2 = Link(2)
    l1.next = l2
    l3 = Link(3)
    l2.next = l3

    new_l = reversed_link(l1)

    t = new_l
    while t:
        print(t.val)
        t = t.next
