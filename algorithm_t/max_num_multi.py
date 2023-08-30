# https://leetcode.cn/problems/integer-break/solution/zheng-shu-chai-fen-by-leetcode-solution/
# 整数拆分，求最大乘积


def max_multi(n):
    dp = [0] * (n + 1)
    for i in range(2, n+1):
        for j in range(i):
            dp[i] = max(dp[i], j * (i - j), j * dp[i-j])
    return dp[n]


if __name__ == '__main__':
    n = 8
    r = max_multi(n)
    print(r)
