class Solution:
    def calc(self, n):
        # 递归
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.calc(n-1) + self.calc(n-2)

    def calc1(self, n):
        # 动态规划，保存每一步计算的值
        t = [0] * 50
        t[0] = 1
        t[1] = 2
        for i in range(2, n):
            t[i] = t[i-1] + t[i-2]
        return t[n-1]
    
    def calc2(self, n):
        # 只用三个变量
        a = 1
        b = 2
        if n == 1:
            return a
        if n == 2:
            return b
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return c


if __name__ == '__main__':
    r = Solution().calc2(35)
    print(r)
