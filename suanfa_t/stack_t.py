# 两个栈实现队列
class Solution:
    def __init__(self) -> None:
        self.s1 = []
        self.s2 = []

    def push(self, val):
        self.s1.append(val)

    def pop(self):
        while self.s1:
            self.s2.append(self.s1.pop())
        res = self.s2.pop()
        while self.s2:
            self.s1.append(self.s2.pop())
        return res


if __name__ == "__main__":
    s = Solution()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.pop())
