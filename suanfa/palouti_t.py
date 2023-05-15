# https://leetcode.cn/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode-solution/
# 爬楼梯：可以一步，两步，三步，求有多少种爬法

def digui_t(n, t):
    # 递归法：引入t，存入计算过的n，时间复杂度由O(2^n)变为O(n)
    if t[n-1] > 0:
        return t[n-1]

    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    t[n-1] = digui_t(n-1, t) + digui_t(n-2, t) + + digui_t(n-3, t)
    return t[n-1]


def dp_t(n):
    # 动态规划
    dp = [0] * n
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4
    for i in range(3, n):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n-1]


if __name__ == '__main__':
    n = 5
    t = [0] * n
    # r = digui_t(n, t)
    r = dp_t(n)
    print(r)
