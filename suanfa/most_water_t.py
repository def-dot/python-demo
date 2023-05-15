# https://leetcode.cn/problems/container-with-most-water/solution/sheng-zui-duo-shui-de-rong-qi-by-leetcode-solution/
# 给定一个数组，求任意两个值之间的面积（按小值计算）


def loop_t(nums):
    # 双循环 复杂度o(n^2)
    res = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if i == j:
                continue
            t = min(nums[i], nums[j]) * (j-i)
            res = max(res, t)
    return res


def double_point_t(nums):
    # 双指针 复杂度o(n)
    res = 0
    i = 0
    j = len(nums) - 1
    while i < j:
        t = min(nums[i], nums[j]) * (j-i)
        res = max(res, t)
        if nums[i] < nums[j]:
            i += 1
        else:
            j -= 1
    return res


nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]


if __name__ == '__main__':
    # res = loop_t(nums)
    res = double_point_t(nums)
    print(res)
