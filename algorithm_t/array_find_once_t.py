# https://leetcode.cn/problems/single-number/
# 一个数组，其中一个元素只出现过一次，其他元素都出现过两次，查找只出现过一次的元素
# 时间复杂度为o(n)，不使用额外的空间（异或计算）
from functools import reduce


def hash_t(nums):
    # 方法1：hash表
    # 时间复杂度o(n)，增加了额外的存储空间ht1，空间复杂度也为o(n)
    ht1 = {}
    for item in nums:
        if item not in ht1:
            ht1[item] = 1
        else:
            ht1[item] += 1

    for k in ht1:
        if ht1[k] == 1:
            print(k)


def xor_t(nums):
    res = reduce(lambda x, y: x^y, nums)
    print(res)


nums = [2, 2, 1]

if __name__ == '__main__':
    # hash_t(nums)
    xor_t(nums)