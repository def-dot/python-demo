"""
动态规划
"""
import time


class Solution:
    def __init__(self):
        self.res = [0, 1]

    def force_t(self, n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return self.force_t(n-2) + self.force_t(n-1)

    def optimize_t(self, n: int) -> int:
        if n <= len(self.res):
            return self.res[n-1]

        r = self.optimize_t(n-2) + self.optimize_t(n-1)
        self.res.append(r)
        return r

    def optimize_t2(self, n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            dp = [0] * n
            dp[0] = 0
            dp[1] = 1
            for i in range(2, n):
                dp[i] = dp[i-1] + dp[i-2]
            return dp[n-1]


if __name__ == '__main__':
    # t1 = time.time()
    # r = Solution().force_t(40)  # r 63245986 cost: 12.171443462371826
    # print(f"r {r} cost: {time.time() - t1}")

    # t1 = time.time()
    # r = Solution().optimize_t(40)  # r 63245986 cost: 0.0
    # print(f"r {r} cost: {time.time() - t1}")

    t1 = time.time()
    r = Solution().optimize_t2(40)  # r 63245986 cost: 0.0
    print(f"r {r} cost: {time.time() - t1}")
