# https://leetcode.cn/problems/min-stack/
# 支持push pop top ，O(1)取最小值


class C:
    def __init__(self):
        self.nums = []
        self.min_nums = []
        self.max_nums = []

    def push(self, val):
        self.nums.append(val)
        if not self.min_nums or val < self.min_nums[-1]:
            self.min_nums.append(val)
        if not self.max_nums or val > self.max_nums[-1]:
            self.max_nums.append(val)

    def top(self):
        return self.nums[-1]

    def pop(self):
        val = self.nums.pop()
        if self.min_nums[-1] == val:
            self.min_nums.pop()

        if self.max_nums[-1] == val:
            self.max_nums.pop()

    def min(self):
        return self.min_nums[-1]

    def max(self):
        return self.max_nums[-1]


if __name__ == '__main__':
    c = C()
    nums = [5, 3, 9, 7]
    for t in nums:
        c.push(t)

    print(c.max())
    c.pop()
    c.pop()
    print(c.max())
