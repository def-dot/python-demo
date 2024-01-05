# 栈，包含push top pop min
class Solution:
    def __init__(self) -> None:
        self.s1 = []
        self.s2 = [] # 存放栈底到当前索引间的最小值

    def push(self, val):
        self.s1.append(val)
        if not self.s2 or self.s2[-1] > val:
            self.s2.append(val)
        else:
            self.s2.append(self.s2[-1])

    def pop(self):
        self.s1.pop()
        self.s2.pop()
    
    def top(self):
        return self.s1[-1]
    
    def min(self):
        return self.s2[-1]


if __name__ == "__main__":
    s = Solution()
    s.push(5)
    s.push(6)
    s.push(2)
    s.push(1)
    s.push(7)
    print(s.min())
    s.pop()
    print(s.min())
    s.pop()
    print(s.min())
    s.pop()
    print(s.min())